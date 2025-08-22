# Object-Detection-and-Avoidance

# 🚀 Mars Rover Autonomous Navigation System

A Python-based system that uses a camera feed to detect objects in real-time and autonomously navigate by avoiding obstacles. The rover moves forward, analyzes video frames continuously, and decides whether to turn and go around objects when detected.

---

## 📑 Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation & Setup](#installation--setup)  
- [How It Works](#how-it-works)  
- [Contributing](#contributing)  

---

## 🛰️ Overview

This project demonstrates a simplified **autonomous navigation system** for a rover using **computer vision**.  
The rover uses its camera to detect objects, track the environment in real-time, and avoid collisions by turning when obstacles are in front.

---

## ⚡ Features

- Real-time **camera feed analysis** using OpenCV  
- **Object detection** with pretrained ML models (YOLO / Haar Cascades / MobileNet-SSD)  
- Decision-making for navigation (**move forward / turn left / turn right**)  
- Extensible for **person-following** or **path planning**  
- Can run on Raspberry Pi, Jetson Nano, or a PC  

---

## 🛠️ Technologies Used

- **Python** – core programming language  
- **OpenCV** – real-time computer vision and image processing  
- **TensorFlow / PyTorch (optional)** – for deep learning object detection models  
- **Raspberry Pi / Jetson Nano (optional)** – for hardware deployment  
- **Serial / GPIO** – for communicating with rover motors  

---

## ⚙️ Installation & Setup

### 1. Clone the Project  
```bash
git clone https://github.com/yourusername/mars-rover-navigation.git
cd mars-rover-navigation
```
### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

pip install -r requirements.txt
```
### 3. Run the Navigation Script
```bash
python rover_navigation.py
```
### 4. Connect Rover Hardware (Optional)

If using Raspberry Pi / Jetson Nano, connect motors via GPIO or serial.

Update the motor_control.py file with correct pin numbers or serial commands.

---

## 🔍 How It Works
1.The rover captures video frames from its camera.

2.Each frame is analyzed using an object detection model (YOLO/SSD).

3.If no object is detected in the front, the rover moves forward.

4.If an object is detected, the rover decides whether to turn left or turn right to avoid it.

5.Loop continues for continuous navigation.

## 🤝 Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

Submit a pull request


