import cv2
import datetime
import os

# Use a working cascade
CASCADE_PATH = r"C:\1python\python projects\python-projects-\cascade.xml"


if not os.path.exists(CASCADE_PATH):
    print("❌ Cascade file not found")
    exit()

cascade = cv2.CascadeClassifier(CASCADE_PATH)

if cascade.empty():
    print("❌ Failed to load cascade")
    exit()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, "Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        print("Detected at:", datetime.datetime.now())

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
