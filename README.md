✋✍️ Air Writing Recognition System (Green
Brush Based)
An AI-powered Air Writing Recognition System that allows users to write characters in the air using a
green-colored pointer/object. The system captures the strokes via a webcam, processes only green
pixels, and recognizes handwritten characters using a custom-trained CNN model.
📌 Features
• 
• 
• 
• 
• 
• 
✅ Air writing using 
green brush detection (HSV-based)
✅ Personal dataset collection
✅ Custom CNN training (TensorFlow/Keras)
✅ Real-time prediction via webcam
✅ Noise-free detection (only green strokes considered)
✅ Works offline
🛠
️ Tech Stack
• 
• 
• 
• 
Python 3.9+
OpenCV – video capture & image processing
NumPy – numerical operations
TensorFlow / Keras – CNN model training & prediction
📂 Project Structure
AirWritingProject/
│
├── air_writing_collect.py      # Collect green air-written samples
├── train_personal_model.py    # Train CNN on collected samples
├── air_writing_predict.py     # Real-time prediction
├── personal_model.h5          # Trained model (generated)
├── labels.txt                 # Class labels
├── samples/                   # Dataset folder
│   ├── A/
│   ├── B/
│   └── C/
├── requirements.txt
└── README.md
1
⚙
️ Installation & Setup
1
️
⃣ Create Virtual Environment (Recommended)
python-m venv airwrite_env
airwrite_env\Scripts\activate
If PowerShell blocks activation, run: 
Set-ExecutionPolicy-Scope CurrentUser-ExecutionPolicy
RemoteSigned
2
️
⃣ Install Requirements
pip install-r requirements.txt
🎨 Step 1: Collect Air-Writing Samples
Run: 
python air_writing_collect.py
Instructions:
• 
• 
• 
• 
Use a green-colored object (pen cap, marker, tape)
Draw characters in the air
Press 
s → enter character label (A, B, C, etc.)
Collect 5–10 samples per character
📁 Images are saved automatically as: 
samples/A/0.png
samples/A/1.png
🧠 Step 2: Train the Model
python train_personal_model.py
2
Output:
• 
• 
• 
• 
Trains a CNN on your samples
Generates:
personal_model.h5
labels.txt
🔮 Step 3: Predict Air-Written Characters
python air_writing_predict.py
Controls:
• 
• 
• 
• 
Move green object → draw
r → recognize character
c → clear canvas
q → quit
Prediction result is printed in the terminal.
🎯 How It Works (Pipeline)
1. 
2. 
3. 
4. 
5. 
6. 
Webcam captures video frames
Convert frames to HSV color space
Extract only green pixels
Draw strokes on virtual canvas
Resize to 28×28 grayscale image
CNN predicts the character
🧪 Model Details
• 
• 
• 
• 
• 
• 
• 
Input shape: 
28 × 28 × 1
Architecture:
Conv2D → MaxPool
Conv2D → MaxPool
Dense → Softmax
Optimizer: Adam
Loss: Categorical Crossentropy
🧠 Viva / Interview Explanation
“The system uses HSV-based green color segmentation to isolate air-written strokes,
which are then classified using a custom-trained convolutional neural network.”
3
�
� Future Enhancements
• 
• 
• 
• 
• 
Word & sentence recognition
Gesture-based space detection
Confidence score display
AR overlay text display
Mobile deployment
👨💻 Author
Rahul Yadav
B.Tech CSE (AI & ML)
📜 License
This project is for academic and educational use only.
✅ Project successfully demonstrates Augmented Reality + Computer Vision + Deep Learning integration.
4
