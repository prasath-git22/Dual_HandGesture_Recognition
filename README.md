# 🤖 Dual Hand Gesture Recognition

A real-time **AI-based dual-hand gesture recognition system** that uses a webcam to detect and classify hand gestures. The project combines **computer vision, machine learning, and automation** to control different computer functions using hand gestures.

## 🚀 Features

* ✋ Real-time dual-hand detection
* 🤏 Hand gesture recognition and classification
* 🎥 Live webcam processing
* 🖱️ Gesture-based mouse control
* ⌨️ Gesture-based keyboard control
* 🔊 Voice interaction
* 💡 Screen brightness control
* 🧠 Machine learning-based gesture classification
* ⚡ Real-time gesture inference

## 🛠️ Technologies Used

| Technology                    | Purpose                              |
| ----------------------------- | ------------------------------------ |
| **Python**                    | Core programming language            |
| **OpenCV**                    | Real-time webcam and computer vision |
| **MediaPipe**                 | Hand detection and landmark tracking |
| **NumPy**                     | Numerical data processing            |
| **Scikit-learn**              | Gesture classification               |
| **PyAutoGUI**                 | Mouse and keyboard automation        |
| **Pickle**                    | Trained model storage                |
| **Screen Brightness Control** | Display brightness adjustment        |

## 🧠 How It Works

The system follows a simple computer-vision and machine-learning pipeline:

```text
Webcam
   ↓
Hand Detection
   ↓
Hand Landmark Extraction
   ↓
Gesture Feature Processing
   ↓
Machine Learning Model
   ↓
Gesture Classification
   ↓
Computer Control Action
```

The webcam captures live video frames, while **MediaPipe** detects the hands and extracts hand landmarks. These features are processed and passed to the trained machine learning model for gesture classification.

Based on the recognized gesture, the application can perform computer-control actions such as mouse movement, keyboard interaction, and brightness adjustment.

## 📂 Project Structure

```text
Dual_HandGesture_Recognition/
│
├── main.py                  # Main application
├── collect_data.py          # Collect gesture training data
├── train_model.py           # Train the gesture classification model
├── gesture_model.pkl        # Trained gesture model
├── gesture_data.csv         # Gesture training dataset
├── gestures.json            # Gesture configuration
├── context.py               # Application context
├── memory.py                # Memory management
├── memory.json              # Stored application data
├── voice_ai.py              # Voice interaction module
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/prasath-git22/Dual_HandGesture_Recognition.git
```

### 2. Navigate to the project

```bash
cd Dual_HandGesture_Recognition
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

Start the main application:

```bash
python main.py
```

Make sure your computer has a working **webcam** before running the application.

## 🧪 Training the Gesture Model

The project includes scripts for collecting gesture data and training the classification model.

### Collect gesture data

```bash
python collect_data.py
```

This script is used to collect hand gesture samples for training.

### Train the model

```bash
python train_model.py
```

The trained model is stored as:

```text
gesture_model.pkl
```

## 🎯 Applications

This project demonstrates how hand gestures can be used as an alternative human-computer interaction method.

Potential applications include:

* 🖥️ Touchless computer interaction
* ♿ Accessibility-focused interfaces
* 🎮 Gesture-based controls
* 🤖 Human-computer interaction
* 🏠 Smart system control
* 💻 Hands-free computer operation

## 🔮 Future Improvements

* Add more hand gestures
* Improve recognition accuracy
* Add customizable gesture-to-action mapping
* Improve multi-hand gesture support
* Add a graphical user interface
* Optimize performance for low-end systems
* Add more accessibility features

## 👨‍💻 Author

**Prasath**

B.Tech – Artificial Intelligence and Data Science

GitHub:
https://github.com/prasath-git22

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

---

### 📌 Project

**Dual Hand Gesture Recognition**
Real-time computer vision + machine learning + gesture-based computer automation.
