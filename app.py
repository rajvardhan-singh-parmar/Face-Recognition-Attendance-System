from flask import Flask, render_template, Response
import cv2, pickle, face_recognition, datetime, csv
import numpy as np

app = Flask(__name__)
camera = cv2.VideoCapture(0)

with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

recorded_names = []

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for (box, face_encoding) in zip(boxes, encodings):
            matches = face_recognition.compare_faces(data["encodings"], face_encoding)
            name = "Unknown"

            if True in matches:
                matchedIdx = matches.index(True)
                name = data["names"][matchedIdx]

                if name not in recorded_names:
                    now = datetime.datetime.now()
                    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
                    with open("attendance.csv", "a", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow([name, dt_string])
                    recorded_names.append(name)

            top, right, bottom, left = box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
