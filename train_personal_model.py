import tensorflow as tf
import cv2, os
import numpy as np

X, y = [], []


labels = sorted([d for d in os.listdir("samples")
                 if os.path.isdir(os.path.join("samples", d))])

label_to_index = {label: i for i, label in enumerate(labels)}

print("Classes found:", labels)

for label in labels:
    folder = os.path.join("samples", label)

    for img_name in os.listdir(folder):

       
        if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        img_path = os.path.join(folder, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        
        if img is None:
            print("⚠️ Skipped unreadable file:", img_path)
            continue

        img = img.astype("float32") / 255.0
        img = cv2.resize(img, (28, 28))

        X.append(img)
        y.append(label_to_index[label])

X = np.array(X).reshape(-1, 28, 28, 1)
y = np.array(y)

print("Total samples:", len(X))


model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(labels), activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X, y, epochs=20, verbose=1)

model.save("personal_model.h5")


with open("labels.txt", "w") as f:
    for label in labels:
        f.write(label + "\n")

print("✅ Training complete")
print("✅ Model saved as personal_model.h5")
print("✅ Labels saved as labels.txt")