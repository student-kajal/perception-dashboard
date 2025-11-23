import cv2
import numpy as np
import open3d as o3d
import plotly.graph_objects as go

def process_image(img_bytes):
    """
    Process 2D image for edge detection and segmentation
    Args:
        img_bytes: Raw image bytes
    Returns:
        orig_img, edges, threshold
    """
    file_bytes = np.asarray(bytearray(img_bytes), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Edge detection using Canny
    edges = cv2.Canny(gray, 50, 150)
    
    # Threshold segmentation
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    
    return img, edges, thresh


def process_point_cloud(ply_path):
    """
    Process 3D point cloud with RANSAC plane segmentation
    Args:
        ply_path: Path to .ply file
    Returns:
        plane_cloud, obstacle_cloud, plane_model, original_points, downsampled_points
    """
    try:
        # Load point cloud
        pcd = o3d.io.read_point_cloud(ply_path)
        num_points = len(pcd.points)
        print(f"✓ Loaded {num_points} points")
        
        # Voxel downsampling for efficiency
        down_pcd = pcd.voxel_down_sample(voxel_size=0.05)
        down_points = len(down_pcd.points)
        print(f"✓ Downsampled to {down_points} points")
        
        # RANSAC plane segmentation
        plane_model, inliers = down_pcd.segment_plane(
            distance_threshold=0.02,
            ransac_n=3,
            num_iterations=1000
        )
        
        print(f"✓ Plane equation: {plane_model}")
        
        # Separate floor (plane) and obstacles
        plane_cloud = down_pcd.select_by_index(inliers)
        obstacle_cloud = down_pcd.select_by_index(inliers, invert=True)
        
        # Color coding: Green = Floor/Safe, Red = Obstacles
        plane_cloud.paint_uniform_color([0, 1, 0])      # Green
        obstacle_cloud.paint_uniform_color([1, 0, 0])   # Red
        
        return plane_cloud, obstacle_cloud, plane_model, num_points, down_points
    
    except Exception as e:
        print(f"✗ Error processing point cloud: {e}")
        return None, None, None, 0, 0


def create_plotly_3d_visualization(plane_cloud, obstacle_cloud):
    """
    Create interactive 3D plot using Plotly (for web deployment)
    Args:
        plane_cloud: Open3D point cloud (floor)
        obstacle_cloud: Open3D point cloud (obstacles)
    Returns:
        Plotly figure object
    """
    # Get point coordinates
    plane_points = np.asarray(plane_cloud.points)
    obstacle_points = np.asarray(obstacle_cloud.points)
    
    # Create figure
    fig = go.Figure()
    
    # Add floor points (green)
    fig.add_trace(go.Scatter3d(
        x=plane_points[:, 0],
        y=plane_points[:, 1],
        z=plane_points[:, 2],
        mode='markers',
        marker=dict(
            size=4,
            color='green',
            opacity=0.8
        ),
        name='Floor/Safe Zone'
    ))
    
    # Add obstacle points (red)
    fig.add_trace(go.Scatter3d(
        x=obstacle_points[:, 0],
        y=obstacle_points[:, 1],
        z=obstacle_points[:, 2],
        mode='markers',
        marker=dict(
            size=4,
            color='red',
            opacity=0.8
        ),
        name='Obstacles'
    ))
    
    # Layout configuration
    fig.update_layout(
        title={
            'text': '3D Point Cloud: RANSAC Plane Detection',
            'x': 0.5,
            'xanchor': 'center'
        },
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            bgcolor='rgba(240, 240, 240, 0.9)',
            xaxis=dict(gridcolor='white', gridwidth=2),
            yaxis=dict(gridcolor='white', gridwidth=2),
            zaxis=dict(gridcolor='white', gridwidth=2)
        ),
        width=900,
        height=700,
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor='rgba(255, 255, 255, 0.8)'
        )
    )
    
    return fig
