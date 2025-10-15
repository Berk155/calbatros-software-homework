import cv2
import numpy as np

weights_path = "yolo/yolov4-tiny.weights"
config_path = "yolo/yolov4-tiny.cfg"
names_path = "yolo/coco.names"

with open(names_path, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

cap = cv2.VideoCapture("image/input_video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids, confidences, boxes = [], [], []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = int(np.argmax(scores))
            confidence = float(scores[class_id])
            if confidence > 0.1:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(confidence)
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.4)

    font = cv2.FONT_HERSHEY_COMPLEX
    best_box, best_conf = None, 0

    if len(indexes) > 0:
        for i in indexes.flatten():
            label = class_names[class_ids[i]]
            if label != "boat":
                continue
            x, y, w, h = boxes[i]
            conf = confidences[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (128, 0, 128), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x, y - 8), font, 0.6, (255, 255, 255), 1)
            if conf > best_conf:
                best_conf = conf
                best_box = (x, y, w, h, label)

    if best_box is not None:
        x, y, w, h, label = best_box
        target_x = int(x + w / 2)
        target_y = int(y + h / 2)
        start_point = (80, height - 80)
        end_point = (target_x, target_y)
        cv2.arrowedLine(frame, start_point, end_point, (0, 255, 0), 3, tipLength=0.1)
        cv2.putText(frame, f"Target: {label}", (30, height - 100), font, 0.7, (0, 255, 0), 2)

    cv2.imshow("yeehaw", frame)

    if cv2.waitKey(int(1000 / cap.get(cv2.CAP_PROP_FPS))) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
