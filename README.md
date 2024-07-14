# CCTV Human Tracker

## Project Description

This project aims to develop a real-time human detection and tracking system using a webcam or video file as input. The system captures video frames, processes each frame to detect humans, and tracks their movements across frames. It utilizes computer vision techniques like HOG descriptor for human detection and CSRT tracker for tracking.

## 🎯 Objective

The objective of this project is to create an automated system that can detect and track humans in real-time, providing a potential tool for surveillance and security applications.

## 🔑 Key Features

- 🎥 Real-time human detection and tracking using a webcam or video file
- 🕵️ Detecting humans using HOG descriptor and SVM
- 🚶‍♂️ Tracking detected humans using CSRT tracker
- 🛠️ Drawing bounding boxes around detected and tracked humans

## 🛠️ Hardware and Software Requirements

### Hardware:
- Webcam or video file

### Software:
- OpenCV
- Tkinter

## 📸 Sample Usage
**Detecting and Tracking Humans**
Run the application, and it will start the webcam feed or process the selected video file. The system will detect humans in the frame, draw bounding boxes around them, and track their movements across frames.

## Dependencies
- OpenCV
- Tkinter

## 🎛️ How to Use

1. **Clone the Repository**

   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/JayxTG/CCTV-Human-Tracker.git
    ```
2. **Install Dependencies**
 Navigate to the project directory and install the required dependencies:

   ```bash
   pip install -r requirements.txt

    ```
3. **Run the Application**
  Execute the main script to start the fall detection system:

   ```bash
   python src/human_tracker.py
   
    ```

## 🏢 Acknowledgments
- OpenCV community for the computer vision tools
- Tkinter community for the graphical user interface tools
