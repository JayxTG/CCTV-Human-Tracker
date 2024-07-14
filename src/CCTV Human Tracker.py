"""

Author: Jayamadu Gammune

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.

"""
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def detect_humans(frame):
    # Convert frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Enhance contrast using histogram equalization
    frame = cv2.equalizeHist(frame)
    
    # Convert frame back to BGR color space
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    # Initialize HOG descriptor and SVM detector for human detection
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Detect humans in the frame using HOG descriptor
    humans, _ = hog.detectMultiScale(frame, winStride=(8, 8), padding=(16, 16), scale=1.05)
    
    return humans

def select_video_file():
    # Create a file dialog to select a video file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
    return file_path

def create_trackers():
    # Create an empty list to store trackers
    trackers = []
    return trackers

def initialize_trackers(trackers, frame, boxes):
    # Initialize trackers for each bounding box in the frame
    for box in boxes:
        tracker = cv2.TrackerCSRT_create()
        trackers.append(tracker)
        tracker.init(frame, tuple(box))
    return trackers

def update_trackers(trackers, frame):
    # Update each tracker and draw bounding box around the tracked object
    for tracker in trackers:
        success, box = tracker.update(frame)
        if success:
            p1 = (int(box[0]), int(box[1]))
            p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2)
            cv2.putText(frame, 'Person', (p1[0], p1[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return frame

def main():
    # Create a root window for the tkinter GUI
    root = tk.Tk()
    root.withdraw()

    # Ask user for video source (webcam or file)
    choice = messagebox.askquestion("Video Source", "Do you want to use webcam as the video source?")

    if choice == 'yes':
        video_source = 0
    else:
        video_file = select_video_file()
        if not video_file:
            print("No video file selected. Exiting.")
            return
        video_source = video_file

    # Open video capture object
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print(f"Error: Could not open video source {video_source}.")
        return

    # Create trackers list
    trackers = create_trackers()

    while True:
        # Read frame from video capture
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame for better visualization
        frame = cv2.resize(frame, (640, 480))

        # Detect humans in the frame
        humans = detect_humans(frame)

        if len(trackers) != len(humans):
            # If number of trackers is different from number of humans detected,
            # recreate trackers and initialize them with new bounding boxes
            trackers = create_trackers()
            for (x, y, w, h) in humans:
                trackers = initialize_trackers(trackers, frame, [(x, y, w, h)])
        else:
            # Update trackers and draw bounding boxes
            frame = update_trackers(trackers, frame)

        # Display frame with bounding boxes
        cv2.imshow('Human Detection and Tracking', frame)

        # Exit loop if 'Esc' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release video capture object and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
