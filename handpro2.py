import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np
wcam,hcam=1000,800
sum=0
sum2=0
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
detector = HandDetector(detectionCon=0.8,maxHands=2)
image1 = cv2.imread("cricbat.png")


#image1=cv2.resize(image1,(1500,900))
cv2.putText(image1, "Player B will BAT", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('image',image1[0:1000, 0:1000])
cv2.waitKey(0)
cv2.destroyAllWindows()
while True:
    while True:
        success, img = cap.read()
        hands = detector.findHands (img,draw=False)

        if hands:

            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            finger1=detector.fingersUp(hand1)

            if(len(hands)==2):
                hand2 = hands[1]
                lmList2 = hand2["lmList"]
                finger2 = detector.fingersUp(hand2)
                print(finger1, finger2)
                if(finger1[0]==finger2[0] and finger1[1]==finger2[1] and finger1[2]==finger2[2] and finger1[3]==finger2[3] and finger1[4]==finger2[4]):
                      #  cv2.putText(img, "OUT!!", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        cv2.waitKey(1000)
                        break
                elif(finger1[0]==0 and finger1[1]==1 and finger1[2]==0 and finger1[3]==0 and finger1[4]==0):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                          #  cv2.putText(img, "You scored 1 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum = sum + 1
                elif (finger1[0] == 0 and finger1[1] == 1 and finger1[2] == 1 and finger1[3] == 0 and finger1[4] == 0):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                         #   cv2.putText(img, "You scored 2 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum = sum + 2
                elif (finger1[0] == 0 and finger1[1] == 1 and finger1[2] == 1 and finger1[3] == 1 and finger1[4] == 0):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                          #  cv2.putText(img, "You scored 3 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum = sum + 3
                elif (finger1[0] == 0 and finger1[1] == 1 and finger1[2] == 1 and finger1[3] == 1 and finger1[4] == 1):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                          #  cv2.putText(img, "You scored 4 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum = sum + 4
                elif (finger1[0] == 1 and finger1[1] == 1 and finger1[2] == 1 and finger1[3] == 1 and finger1[4] == 1):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                          #  cv2.putText(img, "You scored 5 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum = sum + 5
        cv2.putText(img, str(int(sum)), (450, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)
        cv2.putText(img, "PLAYER B(Batting)", (600, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv2.putText(img, "PLAYER A(Balling)", (50, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv2. imshow("Image", img)
        cv2.waitKey(1)

    img2 = np.zeros_like(img)
    image2 = cv2.imread("stuout.jpg")
    rsiz2=(700, 500)
    image2 = cv2.resize(image2,rsiz2 )
    cv2.putText(image2, "PLAYER A has scored {} runs".format(sum), (150, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    cv2.putText(image2, "PLAYER B need {} runs to win!".format(sum + 1), (150, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    cv2.putText(image2, "Press Any Key to Continue!", (150, 140), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
    cv2.imshow('image2', image2[0:wcam, 0:hcam])

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()


    while True:
        success, img = cap.read()
        hands = detector.findHands(img,draw=False)

        if hands:

            hand1 = hands[0]
            lmList1 = hand1["lmList"]


            if (len(hands) == 2):
                hand2 = hands[1]
                lmList2 = hand2["lmList"]
                finger1 = detector.fingersUp(hand1)
                finger2 = detector.fingersUp(hand2)


                if(sum2>sum):
                    break
                elif (finger1[0] == finger2[0] and finger1[1] == finger2[1] and finger1[2] == finger2[2] and finger1[3] == finger2[3] and finger1[4] == finger2[4]):
                  #  cv2.putText(img, "OUT!!", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.waitKey(1000)
                    break
                elif (finger2[0] == 0 and finger2[1] == 1 and finger2[2] == 0 and finger2[3] == 0 and finger2[4] == 0):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                       #     cv2.putText(img, "You scored 1 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum2 = sum2 + 1
                elif (finger2[0] == 0 and finger2[1] == 1 and finger2[2] == 1 and finger2[3] == 0 and finger2[4] == 0):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                        #    cv2.putText(img, "You scored 2 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum2 = sum2 + 2
                elif (finger2[0] == 0 and finger2[1] == 1 and finger2[2] == 1 and finger2[3] == 1 and finger2[4] == 0):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                       #     cv2.putText(img, "You scored 3 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum2 = sum2 + 3
                elif (finger2[0] == 0 and finger2[1] == 1 and finger2[2] == 1 and finger2[3] == 1 and finger2[4] == 1):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                        #    cv2.putText(img, "You scored 4 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum2 = sum2 + 4
                elif (finger2[0] == 1 and finger2[1] == 1 and finger2[2] == 1 and finger2[3] == 1 and finger2[4] == 1):
                    ti1 = time.time()
                    while (int(time.time() - ti1) < 0.4):
                        while (True):
                        #    cv2.putText(img, "You scored 5 run", (90, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            break
                        x111 = 0
                    sum2 = sum2 + 5
        cv2.putText(img, str(int(sum2)), (450, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)
        cv2.putText(img, "PLAYER B(Balling)", (600, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv2.putText(img, "PLAYER A(Batting)", (50, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    img3 = np.zeros_like(img)
    if(sum>sum2):
        image3 = cv2.imread("cup.jpg")

        image3 = cv2.resize(image3, (800, 500))
        cv2.putText(image3,"Congratulations!!Player B has won",(150,300),cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        cv2.imshow('image', image3[0:1000, 0:1000])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif (sum < sum2):
        image3 = cv2.imread("cup.jpg")

        image3 = cv2.resize(image3, (800, 500))
        cv2.putText(image3, "Congratulations!!Player A has won", (150, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        cv2.imshow('image', image3[0:1000, 0:1000])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        image3 = cv2.imread("cup.jpg")

        image3 = cv2.resize(image3, (800, 500))
        cv2.putText(image3, "IT IS A TIE", (150, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        cv2.imshow('image', image3[0:1000, 0:1000])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

