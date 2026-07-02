# 🌍 Multilingual Sign Language Recognition System

A real-time Computer Vision and NLP project that detects hand gestures using a webcam, recognizes numbers from 0 to 10 based on finger count, and converts them into speech in multiple languages.

## 🚀 Features

- Real-time hand detection using MediaPipe
- Finger counting from 0 to 10
- Supports up to 2 hands simultaneously
- Multilingual voice output
- Language switching using keyboard shortcuts
- Gesture stabilization for improved accuracy
- Real-time FPS monitoring
- Professional OpenCV UI
- Voice feedback using Text-to-Speech

---

## 🌐 Supported Languages

| Key | Language |
|-----|----------|
| 1 | English |
| 2 | Hindi |
| 3 | Gujarati |
| 4 | Marathi |
| 5 | French |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| Numerical Operations | NumPy |
| Speech Synthesis | gTTS / pyttsx3 |
| Audio Playback | pygame |
| Concurrency | threading |

---

## 🏗️ System Architecture

```text
Webcam Input
      ↓
OpenCV Frame Capture
      ↓
MediaPipe Hand Detection
      ↓
Extract 21 Hand Landmarks
      ↓
Finger Counting Algorithm
      ↓
Number Recognition (0-10)
      ↓
Language Translation
      ↓
Text-to-Speech Conversion
      ↓
Audio Output
```

---

## 📂 Project Structure

```text
Multilingual-Sign-Language-Recognition-System/
│
├── app.py
│
├── models/
│   └── hand_tracker.py
│
├── utils/
│   ├── finger_counter.py
│   └── language_data.py
│
├── requirements.txt
│
├── README.md
│
└── assets/
```

---

## 🤖 Model Used

### MediaPipe Hands

This project uses the pre-trained MediaPipe Hands model which internally runs using TensorFlow Lite.

Features:

- Detects 21 hand landmarks
- Real-time performance
- No dataset required
- No model training required
- Optimized for CPU inference

---

## 🧠 Algorithm Used

### Finger Counting Algorithm

For Index, Middle, Ring, and Pinky fingers:

```python
if fingertip_y < pip_joint_y:
    finger = open
```

For Thumb:

```python
thumb_tip_x and thumb_ip_x comparison
```

Total fingers:

```python
count = thumb + index + middle + ring + pinky
```

---

## 🎯 Landmark Reference

| Landmark ID | Finger Part |
|------------|------------|
| 0 | Wrist |
| 4 | Thumb Tip |
| 8 | Index Tip |
| 12 | Middle Tip |
| 16 | Ring Tip |
| 20 | Pinky Tip |

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Multilingual-Sign-Language-Recognition-System.git
```

### Navigate to Project Folder

```bash
cd Multilingual-Sign-Language-Recognition-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python app.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| 1 | English |
| 2 | Hindi |
| 3 | Gujarati |
| 4 | Marathi |
| 5 | French |
| Q | Exit Application |

---

## 📈 Performance

| Metric | Value |
|--------|-------|
| FPS | 25-35 |
| Accuracy | 95-98% |
| Maximum Hands | 2 |
| Number Range | 0-10 |

---

## 🔮 Future Improvements

- Alphabet Recognition (A-Z)
- Complete Sign Language Translation
- Sentence Generation
- Transformer-based NLP Models
- Mobile Application Deployment
- Cloud API Integration
- Emotion Detection
- Indian Sign Language Dataset Training

---

## 👨‍💻 Author

Developed by **Krisha Thakar**

---

## 📜 License

This project is licensed under the MIT License.
