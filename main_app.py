import streamlit as st
from perception_utils import process_image, process_point_cloud, create_plotly_3d_visualization
import os

# Page configuration
st.set_page_config(
    page_title="Perception Dashboard",
    page_icon="🤖",
    layout="wide"
)

# Title and header
st.title("🤖 Complete Perception Dashboard")
st.markdown("**2D Image Processing + 3D Point Cloud Analysis | OpenCV + Open3D + Plotly**")
st.markdown("---")

# Section 1: 2D Image Processing
st.header("📷 2D Perception: Edge & Object Detection")
st.markdown("Upload an image to detect edges and segment objects using OpenCV")

upload_img = st.file_uploader(
    "Upload Room/Scene Image", 
    type=["jpg", "png", "jpeg"], 
    key="img"
)

if upload_img:
    orig_img, edges_img, thresh_img = process_image(upload_img.read())
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image(
            orig_img, 
            channels='BGR', 
            caption="Original Image", 
            use_container_width=True
        )
    
    with col2:
        st.image(
            edges_img, 
            channels='GRAY', 
            caption="Edge Detection (Canny)", 
            use_container_width=True
        )
    
    with col3:
        st.image(
            thresh_img, 
            channels='GRAY', 
            caption="Threshold Segmentation", 
            use_container_width=True
        )
    
    st.success("✅ 2D Image Processing Complete!")

else:
    st.info("👆 Upload an image to start 2D perception analysis")

st.markdown("---")

# Section 2: 3D Point Cloud Processing
st.header("🔴 3D Perception: RANSAC Plane Detection")
st.markdown("Upload a .ply point cloud file to detect floor (green) vs obstacles (red)")

ply_file = st.file_uploader(
    "Upload Point Cloud (.ply)", 
    type=["ply"], 
    key="ply"
)

if ply_file:
    # Save uploaded file temporarily
    tmp_path = "temp_cloud.ply"
    with open(tmp_path, "wb") as f:
        f.write(ply_file.read())
    
    # Process point cloud
    with st.spinner("Processing 3D point cloud with RANSAC..."):
        plane_cloud, obstacle_cloud, plane_model, orig_pts, down_pts = process_point_cloud(tmp_path)
    
    if plane_cloud:
        st.success("✅ 3D Point Cloud Processed with RANSAC Plane Segmentation!")
        
        # Display metrics
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Original Points", f"{orig_pts:,}")
            st.metric("Downsampled Points", f"{down_pts:,}")
            st.metric("Floor Points (Green)", f"{len(plane_cloud.points)}")
            st.metric("Obstacle Points (Red)", f"{len(obstacle_cloud.points)}")
        
        with col2:
            st.write("**Detected Plane Equation:**")
            st.code(
                f"{plane_model[0]:.3f}x + {plane_model[1]:.3f}y + "
                f"{plane_model[2]:.3f}z + {plane_model[3]:.3f} = 0",
                language="python"
            )
            st.caption("🟢 Green = Floor/Safe Zone | 🔴 Red = Obstacles")
        
        st.markdown("---")
        
        # Interactive 3D Visualization (Plotly)
        st.subheader("🔍 Interactive 3D Visualization")
        with st.spinner("Rendering 3D view..."):
            fig_3d = create_plotly_3d_visualization(plane_cloud, obstacle_cloud)
            st.plotly_chart(fig_3d, use_container_width=True)
        
        st.caption("💡 **Tip:** Use mouse to rotate, zoom, and pan the 3D view")
        
        # Clean up temp file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    
    else:
        st.error("❌ Error processing point cloud. Please check file format.")

else:
    st.info("👆 Upload a .ply point cloud file to start 3D perception analysis")

# Footer
st.markdown("---")
st.caption(
    "Built with Python, OpenCV, Open3D, Plotly, Streamlit | "
    "Full 2D+3D Perception Pipeline for Autonomous Robotics"
)
