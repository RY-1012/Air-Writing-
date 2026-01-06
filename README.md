<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Air Writing Recognition System</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f4f6f8;
            color: #333;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: auto;
            padding: 30px;
            background: #ffffff;
        }
        h1, h2, h3 {
            color: #0a7d5f;
        }
        h1 {
            border-bottom: 3px solid #0a7d5f;
            padding-bottom: 10px;
        }
        code {
            background: #eee;
            padding: 3px 6px;
            border-radius: 4px;
        }
        pre {
            background: #222;
            color: #f8f8f2;
            padding: 15px;
            overflow-x: auto;
            border-radius: 6px;
        }
        ul {
            margin-left: 20px;
        }
        .section {
            margin-bottom: 30px;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            color: #777;
            font-size: 14px;
        }
        .highlight {
            background: #e8f7f3;
            padding: 10px;
            border-left: 4px solid #0a7d5f;
        }
    </style>
</head>
<body>

<div class="container">

    <h1>✋✍️ Air Writing Recognition System (Green Brush Based)</h1>

    <p class="highlight">
        An AI-powered Air Writing Recognition System that allows users to write characters in the air
        using a green-colored pointer/object. The system captures strokes via a webcam, processes only
        green pixels, and recognizes handwritten characters using a custom-trained CNN model.
    </p>

    <div class="section">
        <h2>📌 Features</h2>
        <ul>
            <li>✅ Air writing using green brush detection (HSV-based)</li>
            <li>✅ Personal dataset collection</li>
            <li>✅ Custom CNN training (TensorFlow / Keras)</li>
            <li>✅ Real-time prediction via webcam</li>
            <li>✅ Noise-free detection (only green strokes considered)</li>
            <li>✅ Works offline</li>
        </ul>
    </div>

    <div class="section">
        <h2>🛠️ Tech Stack</h2>
        <ul>
            <li>Python 3.9+</li>
            <li>OpenCV – video capture & image processing</li>
            <li>NumPy – numerical operations</li>
            <li>TensorFlow / Keras – CNN model training & prediction</li>
        </ul>
    </div>

    <div class="section">
        <h2>📂 Project Structure</h2>
        <pre>
AirWritingProject/
│
├── air_writing_collect.py
├── train_personal_model.py
├── air_writing_predict.py
├── personal_model.h5
├── labels.txt
├── samples/
│   ├── A/
│   ├── B/
│   └── C/
├── requirements.txt
└── README.md
        </pre>
    </div>

    <div class="section">
        <h2>⚙️ Installation & Setup</h2>

        <h3>1️⃣ Create Virtual Environment (Recommended)</h3>
        <pre>
python -m venv airwrite_env
airwrite_env\Scripts\activate
        </pre>
        <p>If PowerShell blocks activation:</p>
        <pre>
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
        </pre>

        <h3>2️⃣ Install Requirements</h3>
        <pre>
pip install -r requirements.txt
        </pre>
    </div>

    <div class="section">
        <h2>🎨 Step 1: Collect Air-Writing Samples</h2>
        <pre>
python air_writing_collect.py
        </pre>
        <ul>
            <li>Use a green-colored object (pen cap, marker, tape)</li>
            <li>Draw characters in the air</li>
            <li>Press <code>s</code> → enter character label (A, B, C, etc.)</li>
            <li>Collect 5–10 samples per character</li>
        </ul>
        <p>Images are saved as:</p>
        <code>samples/A/0.png</code>
    </div>

    <div class="section">
        <h2>🧠 Step 2: Train the Model</h2>
        <pre>
python train_personal_model.py
        </pre>
        <ul>
            <li>Trains a CNN on your samples</li>
            <li>Generates <code>personal_model.h5</code> and <code>labels.txt</code></li>
        </ul>
    </div>

    <div class="section">
        <h2>🔮 Step 3: Predict Air-Written Characters</h2>
        <pre>
python air_writing_predict.py
        </pre>
        <ul>
            <li>Move green object → draw</li>
            <li><code>r</code> → recognize character</li>
            <li><code>c</code> → clear canvas</li>
            <li><code>q</code> → quit</li>
        </ul>
        <p>Prediction is printed in the terminal.</p>
    </div>

    <div class="section">
        <h2>🎯 How It Works (Pipeline)</h2>
        <ol>
            <li>Webcam captures video frames</li>
            <li>Convert frames to HSV color space</li>
            <li>Extract only green pixels</li>
            <li>Draw strokes on virtual canvas</li>
            <li>Resize to 28×28 grayscale image</li>
            <li>CNN predicts the character</li>
        </ol>
    </div>

    <div class="section">
        <h2>🧪 Model Details</h2>
        <ul>
            <li>Input shape: 28 × 28 × 1</li>
            <li>Conv2D → MaxPool</li>
            <li>Conv2D → MaxPool</li>
            <li>Dense → Softmax</li>
            <li>Optimizer: Adam</li>
            <li>Loss: Categorical Crossentropy</li>
        </ul>
    </div>

    <div class="section">
        <h2>🧠 Viva / Interview Explanation</h2>
        <blockquote>
            “The system uses HSV-based green color segmentation to isolate air-written strokes,
            which are then classified using a custom-trained convolutional neural network.”
        </blockquote>
    </div>

    <div class="section">
        <h2>🚀 Future Enhancements</h2>
        <ul>
            <li>Word & sentence recognition</li>
            <li>Gesture-based space detection</li>
            <li>Confidence score display</li>
            <li>AR overlay text display</li>
            <li>Mobile deployment</li>
        </ul>
    </div>

    <div class="section">
        <h2>👨‍💻 Author</h2>
        <p>
            <strong>Rahul Yadav</strong><br>
            B.Tech CSE (AI & ML)
        </p>
    </div>

    <div class="section">
        <h2>📜 License</h2>
        <p>This project is for academic and educational use only.</p>
    </div>

    <footer>
        ✅ Demonstrates Augmented Reality + Computer Vision + Deep Learning integration
    </footer>

</div>

</body>
</html>
