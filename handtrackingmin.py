import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

p_time = 0
c_time = 0

while True:
    success , img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for id, lm in enumerate(hand_landmarks.landmark):
               # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id == 0:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

    c_time = time.time()
    fps = 1/(c_time-p_time)
    p_time = c_time
    cv2.putText(
        img,str(int(fps)),
        (10,70),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (255,0,255),
        3
        )
    cv2.imshow("Image", img)
    cv2.waitKey(1)