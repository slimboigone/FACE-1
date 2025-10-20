import argparse
import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load trained model
# model = load_model("D:/python/Classifier_Model/face1_model.h5")
model = load_model("D:/python/Classifier_Model/face1_model.keras")

# # Static image test
# py try_me_out.py --mode static --image "test/Jensen_Huang.jpg"

# # Live webcam test (no boxes)
# py try_me_out.py --mode live

# # Live webcam test (with face detection boxes)
# py try_me_out.py --mode live_box

# Argument parser setup
parser = argparse.ArgumentParser(description="FACE-1: Age, Gender, and Ethnicity Prediction")
parser.add_argument("--mode", choices=["static", "live", "live_box"], required=True,
                    help="Select test mode: static image, live camera, or live camera with bounding boxes")
parser.add_argument("--image", type=str, help="Path to test image (required for static mode)")
args = parser.parse_args()

# Static Image Test
if args.mode == "static":
    if not args.image:
        raise ValueError("Please provide --image <path> when using static mode.")

    img = Image.open(args.image).convert("RGB").resize((128, 128))
    x = np.expand_dims(np.array(img) / 255.0, axis=0)

    # Predict
    age_pred, gender_pred, race_pred = model.predict(x)
    age = int(age_pred[0][0])
    gender = "Male" if gender_pred[0][0] < 0.5 else "Female"
    race = np.argmax(race_pred[0])

    print(f"Predicted Age: {age}")
    print(f"Predicted Gender: {gender}")
    print(f"Predicted Race Class: {race}")

# Live Camera Test (no boxes)
elif args.mode == "live":
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (128, 128))
        x = np.expand_dims(img / 255.0, axis=0)

        # Predict
        age_pred, gender_pred, race_pred = model.predict(x)
        age = int(age_pred[0][0])
        gender = "Male" if gender_pred[0][0] < 0.5 else "Female"
        race = np.argmax(race_pred[0])

        # Display prediction
        cv2.putText(frame, f"{age}, {gender}, {race}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("UTKFace Prediction (Live)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Live Camera Test (with bounding boxes)
elif args.mode == "live_box":
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (128, 128))
            x_input = np.expand_dims(img / 255.0, axis=0)

            # Predict
            age_pred, gender_pred, race_pred = model.predict(x_input)
            age = int(age_pred[0][0])
            gender = "Male" if gender_pred[0][0] < 0.5 else "Female"
            race = np.argmax(race_pred[0])

            # Draw bounding box and label
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"{age}, {gender}, {race}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("UTKFace Prediction (Live + Boxes)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()