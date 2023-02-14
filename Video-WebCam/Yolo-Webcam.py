from ultralytics import YOLO
import cv2
import cvzone
import math
import time

classNames = ['person', 'bicycle', 'car', 'motorbike', 'airplane', ' bus', 'train', 'truck', 'boat',
              'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat',
              'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
              'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'ball', 'kite', 'baseball bat',
              'glove', 'skateboard', 'surfboard', 'racket', 'bottle', 'glass', 'cup',
              'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli',
              'carrot', 'pizza', 'donut', 'cake', 'chair','sofa', 'plant', 'bed',
              'table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
              'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
              'marker', 'stuff', 'stuff', 'stuff', 'stuff', 'stuff', 'stuff' ]
#Webcam import
# cap = cv2.VideoCapture(0)  # For Webcam
# cap.set(3, 1280)
# cap.set(4, 720)

#Video import
cap = cv2.VideoCapture('../Videos/people.mp4')

model = YOLO("../Yolo-Weights/yolov8n.pt")

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            #Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #print(x1, y1, x2, y2)
            #cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,255), 3)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            #Confidence
            conf = math.ceil((box.conf[0]* 100))/100
            print(conf)


            #Class name
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1.8)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
    
