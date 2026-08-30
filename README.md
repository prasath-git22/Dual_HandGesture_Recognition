# 🤖 Dual Hand Gesture Recognition

A real-time AI-based dual hand gesture recognition system that detects and classifies simultaneous hand gestures using a webcam. The system uses computer vision and machine learning to recognize hand gestures and perform computer control actions.

## 🚀 Features

- ✋ Real-time dual-hand detection
- 🤏 Gesture recognition and classification
- 🎥 Live webcam processing
- 🖱️ Gesture-based mouse control
- ⌨️ Gesture-based keyboard control
- 🔊 Voice interaction
- 💡 Screen brightness control
- 🧠 Trained gesture classification model
- ⚡ Real-time inference

## 🛠️ Technologies Used

- **Python**
- **OpenCV** – Real-time computer vision
- **MediaPipe** – Hand landmark detection
- **NumPy** – Numerical processing
- **PyAutoGUI** – Mouse and keyboard automation
- **Screen Brightness Control** – Brightness adjustment
- **Scikit-learn** – Gesture classification
- **Pickle** – Model storage

## 📂 Project Structure

```text
Dual-Hand-Gesture-Recognition/
│
├── main.py              # Main application
├── collect_data.py      # Collect gesture training data
├── train_model.py       # Train the gesture classification model
├── gesture_model.pkl    # Trained gesture model
├── gesture_data.csv     # Gesture training dataset
├── gestures.json        # Gesture configuration
├── context.py           # Application context
├── memory.py            # Memory management
├── memory.json          # Stored application data
├── voice_ai.py          # Voice interaction module
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
