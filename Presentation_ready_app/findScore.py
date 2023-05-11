import cv2
from ultralytics import YOLO
import cv2
import cvzone
import math

classNames = ['10C', '10D', '10H', '10S',
                  '2C', '2D', '2H', '2S',
                  '3C', '3D', '3H', '3S',
                  '4C', '4D', '4H', '4S',
                  '5C', '5D', '5H', '5S',
                  '6C', '6D', '6H', '6S',
                  '7C', '7D', '7H', '7S',
                  '8C', '8D', '8H', '8S',
                  '9C', '9D', '9H', '9S',
                  'AC', 'AD', 'AH', 'AS',
                  'JC', 'JD', 'JH', 'JS',
                  'KC', 'KD', 'KH', 'KS',
                  'QC', 'QD', 'QH', 'QS']

# This function calculates the score (player/dealer)
# At this point it reads 'A' as a 10 / Will work on logic

def findBlackjackScore(hand):
    ranks = []
    suits = []
    values = []
    value = 0
    total = 0

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
            if rank == "A" or rank == "J" or rank == "Q" or rank == "K":
                value = 10
            else:
                value = int(rank)

        else:
            rank = card[0:2]
            suit = card[2]
            if rank == "A" or rank == "J" or rank == "Q" or rank == "K":
                value = 10
            else:
                value = int(rank)
        
        values.append(value)

    #print(values)

    for value in values:
        total = total + value

    #print(total)

    return total


# This function adds up the cards dealt and returns the
# running deck (Counts cards)

def running_count(deck):
    values = []
    count = 0
    value = 0

    for card in deck:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
            if rank == 'A' or rank == 'J' or rank == 'Q' or rank == 'K':
                value = -1

            elif rank == '7' or rank == '8' or rank == '9':
                value = 0

            else:
                value = 1

        else:
            rank = card[0:2]
            suit = card[2]
            if rank == 'A' or rank == 'J' or rank == 'Q' or rank == 'K':
                value = -1

            elif rank == '7' or rank == '8' or rank == '9':
                value = 0

            else:
                value = 1

        values.append(value)

    for v in values:
        count = count + v

    return count


def app(filepath):
    # Video import #Webcam import  *****UNCOMENT THIS BLOCK TO USE VIDEO FILE MAKE SURE TO COMENT OUT THE WEBCAM IMPORT BLOCK******
    # I uploaded some test videos on GitHub, but it should work on any mp4
    path = filepath
    video_file = cv2.VideoCapture(path)

    # Load the YOLO trained model from Yolo-Weights fite (Check Github)
    model = YOLO("CardsModelNano.pt")

    # Create masks
    dealer_mask = cv2.imread('../images/dealer_mask1.png')
    player_mask = cv2.imread('../images/player_mask1.png')
    deck = []  # Empty list to keep track of all the cards dealt (player and dealer)

    # Loop to display images, add boxes and labels
    while True:
        success, img = video_file.read()  # Read image from video file
        imgDealerRegion = cv2.bitwise_and(img, dealer_mask)  # Do a bitwise addition of dealer_mask and image
        imgPlayerRegion = cv2.bitwise_and(img, player_mask)  # Do a bitwise operation of player mask and image
        results_dealer = model(imgDealerRegion, stream=True)  # Feed masked image so it only detects dealers hand
        results_player = model(imgPlayerRegion, stream=True)  # Feed masked image so it only detects players hand
        player_hand = []  # Empty list for players hand
        dealer_hand = []  # Empty list for dealers hand

        # Run detection for dealer
        for r in results_dealer:
            boxes = r.boxes
            for box in boxes:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # print(x1, y1, x2, y2)
                # cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,255), 3)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 0))

                # Confidence value display
                conf = math.ceil((box.conf[0] * 100)) / 100
                # print(conf)

                # Class name (From hard coded classes, Doesn't work too good, but it works)
                cls = int(box.cls[0])
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1.8)

                if conf > 0.5:
                    dealer_hand.append(classNames[cls])  # Add the detected card to the dealer_hand list
                    deck.append(classNames[cls])  # Add the card to the deck list

        # Run detection for player
        for r in results_player:
            boxes = r.boxes
            for box in boxes:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # print(x1, y1, x2, y2)
                # cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,255), 3)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(0, 0, 255))

                # Confidence value display
                conf = math.ceil((box.conf[0] * 100)) / 100
                # print(conf)

                # Class name (From hard coded classes, Doesn't work too good, but it works)
                cls = int(box.cls[0])
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1.8)

                if conf > 0.5:
                    player_hand.append(classNames[cls])  # Add card to player_hand list
                    deck.append(classNames[cls])  # Add card to deck list

        # Turn lists into set to delete duplicates
        player_hand = list(set(player_hand))
        # print(player_hand) # Print statement for testing
        dealer_hand = list(set(dealer_hand))
        # print(dealer_hand)  # Print statement for testing
        deck = list(set(deck))
        # print(f'deck: {deck}')  # Print statement for testing

        # Get player score and print results to screen
        player_results = findBlackjackScore(player_hand)
        print(player_results)
        if player_results <= 21:
            cvzone.putTextRect(img, f'Player: {player_results} ', (20, 50), scale=1.8)
        else:
            cvzone.putTextRect(img, 'Player Bust', (20, 50), scale=1.8)

        # Get dealer score and print results to screen
        dealer_results = findBlackjackScore(dealer_hand)
        print(dealer_results)
        if dealer_results <= 21:
            cvzone.putTextRect(img, f'Dealer: {dealer_results} ', (20, 80), scale=1.8)
        else:
            cvzone.putTextRect(img, 'Dealer Bust', (20, 80), scale=1.8)

        # Get the total deck count and show on screen
        count = running_count(deck)
        # print(f'count: {count}') # Print statement for testing
        cvzone.putTextRect(img, f'Running Count: {count}', (20, 110), scale=1.8)

        # Display the video
        cv2.imshow('Image', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    video_file.release()
    cv2.destroyAllWindows()
    
    
def app_webcam():

    deck = []
    counter = 0

    # Webcam import
    cap = cv2.VideoCapture(0)  # For Webcam
    cap.set(3, 1280)
    cap.set(4, 720)

    # Load the YOLO trained model from Yolo-Weights fite (Check Github)
    model = YOLO("CardsModelNano.pt")


    # Loop to display images, add boxes and labels
    while True:
        success, img = cap.read()
        results = model(img, stream=True)
        detections = np.empty((0, 5))
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
                cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(0, 0, 255))

                # Confidence value display
                conf = math.ceil((box.conf[0] * 100)) / 100
                # print(conf)

                # Class name (From hard coded classes, Doesn't work too good, but it works)
                cls = int(box.cls[0])
                # cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1.8)

                if conf > 0.5:
                    hand.append(classNames[cls])

                if conf > 0.3:
                    deck.append(classNames[cls])

        hand = list(set(hand))
        deck = list(set(deck))
        print(f'hand: {hand}')
        print(f'deck: {deck}')

        score = findBlackjackScore(hand)
        count = running_count(deck)
        print(score)
        print(count)

        cvzone.putTextRect(img, f'Running Count: {count} ', (20, 80), scale=1, thickness=1)

        if score <= 21:
            cvzone.putTextRect(img, f'Score: {score} ', (20, 50), scale=1.8)
        else:
            cvzone.putTextRect(img, 'BUST', (20, 50), scale=1.8)

        # Display the video
        cvzone.putTextRect(img, f'{counter}', (20, 110), scale=1.8)
        cv2.imshow('Image', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    cap.release()
    cv2.destroyAllWindows()
        

        
   
def select_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)

    findScore.app(file_path)
    
    

if __name__ =='__main__':

    findBlackjackScore()

    running_count()

    app()

    app_webcam()
    
    select_file()
