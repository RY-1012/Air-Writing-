import cv2
import numpy as np
import tensorflow as tf


with open("labels.txt", "r") as f:
    LABELS = [line.strip() for line in f]


model = tf.keras.models.load_model("personal_model.h5")


lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])

W, H = 640, 480
BRUSH = 6


canvas = np.zeros((H, W, 3), np.uint8)
prev_point = None

cap = cv2.VideoCapture(0)
print("Controls: r=recognize | c=clear | q=quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if cnts:
        c = max(cnts, key=cv2.contourArea)
        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)
            center = (x + w // 2, y + h // 2)

            if prev_point is not None:
                
                cv2.line(canvas, prev_point, center, (0, 255, 0), BRUSH)

            prev_point = center
            cv2.circle(frame, center, 5, (0, 255, 0), -1)
    else:
        prev_point = None

    frame = cv2.add(frame, canvas)

    cv2.putText(frame, "r=recognize  c=clear  q=quit",
                (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 255), 2)

    cv2.imshow("Air Writing - Predict", frame)

    key = cv2.waitKey(1) & 0xFF

    
    if key == ord('r'):
        
        hsv_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2HSV)
        green_mask = cv2.inRange(hsv_canvas, lower_green, upper_green)

        img = cv2.resize(green_mask, (28, 28))
        img = img.astype("float32") / 255.0
        img = img.reshape(1, 28, 28, 1)

        pred = model.predict(img, verbose=0)
        result = LABELS[np.argmax(pred)]

        print("📝 Recognized Character:", result)

        canvas[:] = 0

    elif key == ord('c'):
        canvas[:] = 0

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()