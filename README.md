#  Air Writing Recognition System (Green Brush Based)

An **AI-powered Air Writing Recognition System** that allows users to write characters in the air using a **green-colored pointer/object**.  
The system captures strokes via a webcam, processes only green pixels, and recognizes handwritten characters using a **custom-trained CNN model**.


## Sample Output
![Image]=(https://github.com/user-attachments/assets/d743167e-935d-4665-af47-cf9c362b7e5d)

---

## 📌 Features

- ✅ Air writing using **green brush detection (HSV-based)**
- ✅ Personal dataset collection
- ✅ Custom CNN training (**TensorFlow / Keras**)
- ✅ Real-time prediction via webcam
- ✅ Noise-free detection (only green strokes considered)
- ✅ Works offline

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **OpenCV** – video capture & image processing
- **NumPy** – numerical operations
- **TensorFlow / Keras** – CNN model training & prediction

---

## 📂 Project Structure

AirWritingProject/
│
├── air_writing_collect.py # Collect green air-written samples
├── train_personal_model.py # Train CNN on collected samples
├── air_writing_predict.py # Real-time prediction
├── personal_model.h5 # Trained model (generated)
├── labels.txt # Class labels
├── samples/ # Dataset folder
│ ├── A/
│ ├── B/
│ └── C/
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup
2️⃣ Install Requirements
pip install -r requirements.txt

python air_writing_collect.py

##Instructions

Use a green-colored object (pen cap, marker, tape)

Draw characters in the air

Press s → enter character label (A, B, C, etc.)

Collect 5–10 samples per character

## 🧠 Step 2: Train the Model
python train_personal_model.py

##Output

Trains a CNN on your samples

Generates:

personal_model.h5

labels.txt

##🔮 Step 3: Predict Air-Written Characters
python air_writing_predict.py

Controls

Move green object → draw

r → recognize character

c → clear canvas

q → quit

Prediction result is printed in the terminal.

##🎯 How It Works (Pipeline)

Webcam captures video frames

Convert frames to HSV color space

Extract only green pixels

Draw strokes on a virtual canvas

Resize to 28×28 grayscale image

CNN predicts the character.

##🧪 Model Details

Input Shape: 28 × 28 × 1

Architecture:

Conv2D → MaxPooling

Conv2D → MaxPooling

Dense → Softmax

Optimizer: Adam

Loss Function: Categorical Crossentropy

##👨‍💻 Author

Rahul Yadav
B.Tech CSE (AI & ML)

Atharva Ghayal
B.tech CSE (AI & DS)

Kavin Nadar
B.tech CSE (AI & ML)

Branden Machado
B.tech CSE (AI & ML)
