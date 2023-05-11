import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *
import time


def people_tracker():
    classNames = ["person", "bicycle", "car", "motorcycle", "plane", "bus", "train", "truck", "boat",
                  "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                  "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
                  "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "ball", "kite", "baseball bat",
                  "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                  "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
                  "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "plant", "bed",
                  "table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
                  "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                  "teddy bear", "hair drier", "toothbrush"
                  ]

    # Tracking
    tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)


    limits = [400, 500, 1500, 500]

    total_count = []

 # Load mask image
    mask = cv2.imread('../images/door_mask.png')

    ################################################################################################
    # USE THIS BLOCK IF YOU NEED TO CROP IMAGE
    # IMAGE AND VIDEO NEED TO BE SAME SIZE OTHERWHISE IT WON'T WORK
    ################################################################################################

    # Convert from BGR to RGB

    # mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

    # Crop it to match image size
    # crop_mask = mask[:720, :1280]

    ####End of block

    ################################################################################################################
    # Webcam import  *****UNCOMENT THIS BLOCK TO USE WEB CAM MAKE SURE TO COMENT OUT THE VIDEO IMPORT BLOCK******
    # for VideoCapture() function pass a 0 if using builtin camera (laptop). Pass 1 or 2 if using USB cam
    ###############################################################################################################
    # cap = cv2.VideoCapture(0)
    # cap.set(3, 1280)
    # cap.set(4, 720)

    #########################################################################################################################
    # Video import #Webcam import  *****UNCOMENT THIS BLOCK TO USE VIDEO FILE MAKE SURE TO COMENT OUT THE WEBCAM IMPORT BLOCK******
    # I uploaded some test videos on GitHub, but it should work on any mp4
    ##############################################################################################################################
    cap = cv2.VideoCapture('../videos/door.mp4')

    # Load the YOLO trained model from Yolo-Weights fite (Check Github)
    model = YOLO("../Yolo-Weights/yolov8n.pt")

    # Use this after you create a Yolo-Weights folder to save your yolo file generated after you run your app 1st time
    # Makes it so you don't have to build model every time **MAKE SURE TO COMMENT OUT THE PREVIOUS model BLOCK
    # model = YOLO("../Yolo-Weights/yolov8n.pt")

    # Loop to display images, add boxes and labels
    while True:
        success, img = cap.read()
        # Perform a bitwise operation to overlay the mask and video feeds
        imgRegion = cv2.bitwise_and(img, mask)

        # Stream the results / pass the imgRegion to show mask
        results = model(imgRegion, stream=True)

        detections = np.empty((0, 5))

        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # print(x1, y1, x2, y2)
                # cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,255), 3)
                w, h = x2 - x1, y2 - y1
                # cvzone.cornerRect(img, (x1, y1, w, h), l=9)

                # Confidence value display
                conf = math.ceil((box.conf[0] * 100)) / 100
                print(conf)

                # Class name (From hard coded classes, Doesn't work too good, but it works)
                cls = int(box.cls[0])
                currentClass = classNames[cls]

                if currentClass == "person" and conf > 0.4:
                    # cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)), scale=0.6, thickness=1, offset=3)
                    # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt= 5)
                    currentArray = np.array([x1, y1, x2, y2, conf])
                    detections = np.vstack((detections, currentArray))

        resultsTracker = tracker.update(detections)
        cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5)


        for result in resultsTracker:
            x1, y1, x2, y2, Id = result
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(result)
            w, h = x2 - x1, y2 - y1

            cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 0))
            cvzone.putTextRect(img, f'{int(Id)}', (max(0, x1), max(35, y1)), scale=0.6, thickness=1, offset=3)

            cx, cy = x1 + w // 2, y1 + h // 2
            # cv2.circle(img, (cx, cy), 5, (255,0,255), cv2.FILLED)

            if limits[0] < cx < limits[2] and limits[1] - 20 < cy < limits[1] + 20:
                if total_count.count(Id) == 0:
                    total_count.append(Id)



        cvzone.putTextRect(img, f'Headcount : {len(total_count)}', (50, 50))

        # Display the video
        cv2.imshow('Image', img)
        # cv2.imshow('ImageRegion', imgRegion)
        #cv2.waitKey(1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    people_tracker()

