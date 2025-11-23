🚀 Complete Perception Dashboard
2D Image Processing + 3D LiDAR Point Cloud Analysis

OpenCV + Open3D + Plotly + Streamlit
---
✨ Project Overview

This project is a full perception system designed for autonomous robots, drones, AGVs, and self-driving vehicles.

It integrates camera-based 2D perception and LiDAR-based 3D point cloud understanding into a single interactive dashboard.

⭐ The system can:

Detect edges and object boundaries from 2D images

Identify floor vs obstacles from 3D LiDAR point clouds

Visualize everything live inside a Streamlit web app

🔧 Real-world Applications:

Self-driving car navigation

Indoor robot pathfinding

Drone landing zone detection

Warehouse robot obstacle avoidance
---
🧠 Architecture
                          ┌────────────────────────────────────────┐
                          │         Perception Dashboard            │
                          └────────────────────────────────────────┘
                                       │              │
                       ┌───────────────┘              └────────────────┐
                       ▼                                                 ▼

         ┌──────────────────────────┐                   ┌──────────────────────────┐
         │       2D Perception      │                   │       3D Perception      │
         ├──────────────────────────┤                   ├──────────────────────────┤
         │ • OpenCV (Canny, Blur)   │                   │ • Open3D Point Clouds    │
         │ • Thresholding           │                   │ • Voxel Downsampling     │
         │ • Edge Detection         │                   │ • RANSAC Plane Fit       │
         └──────────────────────────┘                   └──────────────────────────┘

                                       ▼
                          ┌───────────────────────────────┐
                          │       Streamlit Web UI         │
                          │  (Interactive Visualizations)   │
                          └───────────────────────────────┘
---
🚀 Features
🎯 2D Perception (OpenCV)

Image Upload

Grayscale conversion

Gaussian blur

Canny edge detection

Threshold segmentation

Side-by-side visual comparison

🎯 3D Perception (Open3D)

.ply point cloud upload

Voxel grid downsampling

RANSAC plane detection (floor/wall/table)

Segmentation:

Green → Floor (safe surface)

Red → Obstacles (unsafe)

🎯 Visualization (Plotly)

3D scatter plots

Fully rotatable, zoomable

Works on browser and cloud

🎯 Streamlit Dashboard

Clean UI

Real-time updates

Runs locally or on Streamlit Cloud
---
🛠 Tech Stack
| Component           | Tools       |
| ------------------- | ----------- |
| Web UI              | Streamlit   |
| 2D CV               | OpenCV      |
| 3D Perception       | Open3D      |
| Visualization       | Plotly      |
| Backend             | Python 3.12 |
| Numerical Computing | NumPy       |
---
💻 How to Run
1️⃣ Clone the repository
git clone https://github.com/student-kajal/perception-dashboard.git
cd perception-dashboard
2️⃣ Install dependencies
pip install -r requirements.txt
⚠ Python 3.12 recommended (Open3D compatibility)
3️⃣ Run the dashboard
streamlit run main_app.py
---
📊 Example Outputs
2D Image Processing

<img width="931" height="445" alt="image" src="https://github.com/user-attachments/assets/62eed62b-b974-4115-b72c-234a4f162417" />

3D interactive plot
<img width="924" height="387" alt="image" src="https://github.com/user-attachments/assets/27577b0b-ed8e-428b-9959-bb01bb170d62" />
---
📂 Folder Structure
perception-dashboard/
│
├── main_app.py                # Streamlit UI
├── perception_utils.py        # 2D + 3D processing functions
├── sample_room.ply            # Example point cloud
├── requirements.txt           
└── README.md                  
---
🔬 Algorithms Used
🔹 1. Canny Edge Detection (OpenCV)

Used for 2D object boundary extraction.
Steps:
1. Noise reduction
2. Gradient computation
3. Non-max suppression
4. Edge hysteresis
🔹 2. Voxel Downsampling (Open3D)

Reduces point cloud size with minimal accuracy loss.

🔹 3. RANSAC Plane Fitting

Used to detect the dominant plane (floor) in a noisy LiDAR scan.

Process:
Randomly pick 3 points

Fit a plane

Count inliers

Repeat 1000 times

Best plane = floor
Formula:
ax + by + cz + d = 0
---
🚀 Real-World Use Cases

Autonomous vehicle navigation

Drone landing zone detection

Indoor robot mapping (SLAM support)

Warehouse robotics

Industrial environment modeling
---
🎓 Key Learnings

2D + 3D fusion concepts

Working with LiDAR point clouds

RANSAC in noisy environments

Real-time robotics dashboards

Spatial reasoning in 3D

This project directly matches Perception Engineer responsibilities:
✔ 3D geometry
✔ LiDAR data processing
✔ Image segmentation
✔ Visualization
✔ Python + CV libraries
---
👩‍💻 Author

Kajal Kumari
B.Tech (ECE), NSUT Delhi
🔗 GitHub: https://github.com/student-kajal
---
📜 License

MIT License
---
🙏 Credits

Built using:

OpenCV

Open3D

Plotly

Streamlit

Python

Inspired by real perception stacks in autonomous robots.

