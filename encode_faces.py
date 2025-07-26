import face_recognition, os, cv2, pickle

knownEncodings = []
knownNames = []

dataset = "dataset"

for person in os.listdir(dataset):
    for img_name in os.listdir(f"{dataset}/{person}"):
        img_path = f"{dataset}/{person}/{img_name}"
        image = cv2.imread(img_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for enc in encodings:
            knownEncodings.append(enc)
            knownNames.append(person)

data = {"encodings": knownEncodings, "names": knownNames}
with open("encodings.pickle", "wb") as f:
    f.write(pickle.dumps(data))

print("[INFO] Encodings generated.")
