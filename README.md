# 🚶‍♂️ Moving Object Detection using OpenCV (Python)

## 📌 Overview

This project implements **real-time moving object detection** using a webcam feed and **OpenCV** in Python.
It works by comparing a static background frame with the current frame to detect motion and highlight moving objects using bounding boxes.

The system is lightweight, efficient, and suitable for **basic surveillance**, **security systems**, and **computer vision learning projects**.

---

## 🎯 Features

* 📹 Real-time webcam video processing
* 🖼️ Background frame initialization
* 🔍 Motion detection using frame differencing
* 📦 Bounding boxes around moving objects
* ⚡ Noise reduction using Gaussian blur & dilation
* 🟢 Visual alert when movement is detected

---

## 🛠️ Technologies Used

* Python 3.x
* OpenCV (cv2)
* imutils
* NumPy

---

## 📂 Project Structure

```
moving-object-detection/
│
├── motion_detection.py      # Main Python script
├── README.md                # Project documentation
└── requirements.txt         # Required libraries
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/moving-object-detection.git
cd moving-object-detection
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install opencv-python imutils numpy
```

---

## ▶️ How It Works

1. Captures video frames from the webcam
2. Converts frames to grayscale
3. Applies Gaussian blur to reduce noise
4. Stores the first frame as a **background reference**
5. Computes absolute difference between frames
6. Thresholds and dilates the image to detect motion
7. Draws bounding boxes around detected objects

---

## ▶️ Usage

Run the Python script:

```bash
python motion_detection.py
```

* Press **`Q`** to exit the application.

---

## 🔧 Important Parameters

| Parameter              | Description                                  |
| ---------------------- | -------------------------------------------- |
| `area = 500`           | Minimum contour area to be considered motion |
| `GaussianBlur (21,21)` | Noise reduction strength                     |
| `threshold = 25`       | Motion sensitivity                           |

You can fine-tune these values based on lighting and camera quality.

---

## 📸 Output

* Green rectangles around moving objects
* Red text **"Movement Detected"** displayed on motion

---

## ⚠️ Limitations

* Sensitive to lighting changes
* Static background assumption
* Not suitable for crowded environments
* Detects motion, not object type

---

## 🚀 Future Enhancements

* 🔥 Deep Learning-based object detection (YOLO / SSD)
* 📤 Email or alarm notifications
* 📁 Video recording on motion detection
* 🎯 Object classification (Human, Vehicle, Animal)
* 🧠 Background updating mechanism

---

## 👨‍💻 Author

Aadhavan S
ECE | AI | Computer Vision | ML | Edge AI Enthusiast

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.

---

