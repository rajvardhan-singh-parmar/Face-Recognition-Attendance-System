# Face-Recognition-Attendance-System 


# Face Recognition Attendance System

A Python-based smart attendance system using face recognition to mark student or employee attendance automatically through a webcam feed.

## 📌 Features

- Real-time face detection & recognition using OpenCV and face_recognition.
- Mark attendance with date and time.
- Avoid duplicate attendance on the same day.
- Simple Flask web interface with live camera feed.
- Export attendance to CSV file.

## 🛠 Tech Stack

- **Language:** Python
- **Libraries:** OpenCV, face_recognition, Flask, NumPy, Pandas
- **Frontend:** HTML (Jinja template), CSS
- **Database:** CSV (for attendance log)

## 📁 Project Structure

```
Face-Recognition-Attendance-System/
├── app.py                  # Main Flask application
├── encode_faces.py         # Script to encode known faces from dataset
├── requirements.txt        # Required Python packages
├── attendance.csv          # CSV file to store attendance logs
├── encodings.pickle        # Stored encodings of known faces
├── dataset/                # Folder containing known user images
│   └── Rajvardhan/
├── static/
│   └── style.css           # (Optional) Styling
├── templates/
│   └── index.html          # Flask HTML template
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add face images
Place your face images inside `dataset/<YourName>/` folder. Example:
```
dataset/Rajvardhan/
    - img1.jpg
    - img2.jpg
```

### 4. Encode known faces
```bash
python encode_faces.py
```

### 5. Run the web app
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 📝 Attendance Format (CSV)
```
Name,DateTime
Rajvardhan,2025-07-26 10:45:32
```

## 📦 Future Enhancements

- Admin dashboard with login
- SQLite/MySQL backend
- Facial spoofing detection
- Real-time email or SMS notifications
- Export attendance in Excel or PDF

---

© 2025 Rajvardhan Singh Parmar | All Rights Reserved
