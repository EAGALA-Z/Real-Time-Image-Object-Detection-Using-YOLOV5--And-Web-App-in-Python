# 🧠 Real-Time Object Detection using YOLOv5 + Streamlit

This project is a real-time object detection web app built using **YOLOv5**, **OpenCV**, and **Streamlit**. It supports both static image detection and webcam-based live detection using WebRTC.

<br>

## 📸 Features

- 🔍 Detect objects in images using pre-trained YOLOv5 ONNX models  
- 🎥 Real-time detection via webcam using `streamlit-webrtc`  
- 📂 Upload and analyze images directly from the web UI  
- 🖼️ Bounding boxes with labels and confidence scores  
- ⚙️ Easy to configure and extend for custom models  

<br>

## 🛠️ Tech Stack

- Python  
- YOLOv5 
- OpenCV  
- Streamlit  
- streamlit-webrtc  
- PyTorch  
- Pillow  

<br>

## 📦 Installation

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

<br>

## ▶️ Run the App

```bash
streamlit run app.py
```

Or for webcam detection (YOLO + WebRTC):

```bash
streamlit run pages/2_YOLO_webrtc.py
```

<br>

## 📁 Project Structure

```bash
├── __pycache__/
├── app.py                         # Main entry point
├── yolo_predictions.py           # YOLO logic class
├── requirements.txt              # Dependencies
├── README.md                     # Project documentation
│
├── pages/
│   ├── 1_YOLO_for_image.py       # Image upload & detection
│   ├── 2_YOLO_webrtc.py          # Real-time webcam detection
│   └── 3_About.py                # About page
│
├── models/
│   ├── best.onnx                 # ONNX model
│   └── data.yaml                 # Class labels and configs
│
├── images/                       # Icons and page images
│   ├── about.png
│   ├── camera.png
│   ├── home.png
│   └── object.png
│
├── media/                        # Sample test images & videos
│   ├── *.jpg / *.jpeg / *.webp / *.mp4
│   └── zeena.jpg              
```

<br>

## 📌 Notes

- Ensure your `yolov5` model and `data.yaml` file are correctly placed in the `model/` directory.
- If using on Streamlit Cloud, ensure the ONNX model is below 100MB (or use external hosting).

<br>

## 🙌 Acknowledgements

- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)  
- [Streamlit](https://streamlit.io)
