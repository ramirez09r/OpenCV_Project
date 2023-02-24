from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import test

# I hard coded these classes, there are many ways to do this, I just decided to do it the fu** it way

classNames= ['10c', '10d', '10h', '10s',
             '2c', '2d', '2h', '2s',
             '3c', '3d', '3h', '3s',
             '4c', '4d', '4h', '4s',
             '5c', '5d', '5h', '5s',
             '6c', '6d', '6h', '6s',
             '7c', '7d', '7h', '7s',
             '8c', '8d', '8h', '8s',
             '9c', '9d', '9h', '9s',
             'Ac', 'Ad', 'Ah', 'As',
             'Jc', 'Jd', 'Jh', 'Js',
             'Kc', 'Kd', 'Kh', 'Ks',
             'Qc', 'Qd', 'Qh', 'Qs']



# Webcam import  *****UNCOMENT THIS BLOCK TO USE WEB CAM MAKE SURE TO COMENT OUT THE VIDEO IMPORT BLOCK******
#cap = cv2.VideoCapture(2)  # For Webcam
# cap.set(3, 1280)
# cap.set(4, 720)

# Video import #Webcam import  *****UNCOMENT THIS BLOCK TO USE VIDEO FILE MAKE SURE TO COMENT OUT THE WEBCAM IMPORT BLOCK******
# I uploaded some test videos on GitHub, but it should work on any mp4
cap = cv2.VideoCapture('../Videos/blackjackL.mp4')

# Load the YOLO trained model from Yolo-Weights fite (Check Github)
model = YOLO("../Yolo-Weights/playingCards.pt")

# Use this after you create a Yolo-Weights folder to save your yolo file generated after you run your app 1st time
# Makes it so you don't have to build model every time **MAKE SURE TO COMMENT OUT THE PREVIOUS model BLOCK
# model = YOLO("../Yolo-Weights/yolov8n.pt")


# Loop to display images, add boxes and labels
while True:
    success, img = cap.read()
    results = model(img, stream=True)
    hand = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # print(x1, y1, x2, y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,255), 3)
            w, h = x2 - x1, y2 - y1
            #cvzone.cornerRect(img, (x1, y1, w, h))

            # Confidence value display
            conf = math.ceil((box.conf[0] * 100)) / 100
            #print(conf)

            # Class name (From hard coded classes, Doesn't work too good, but it works)
            cls = int(box.cls[0])
            #cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1.8)

            if conf > 0.5:
                hand.append(classNames[cls])



    hand = list(set(hand))
    print(hand)


    results = test.findBlackjackScore(hand)
    print(results)
    if results <= 21:
        cvzone.putTextRect(img, f'{results} ', (20, 50), scale=1.8)
    else:
        cvzone.putTextRect(img, 'BUST', (20, 50), scale=1.8)
    # Display the video
    cv2.imshow('Image', img)
    cv2.waitKey(1)