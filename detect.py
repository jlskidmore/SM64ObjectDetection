from cv2 import cv2

mario_cascade = cv2.CascadeClassifier('/home/logan/Projects/sm64_object_detection/mario_cascade.xml')
coin_cascade = cv2.CascadeClassifier('/home/logan/Projects/sm64_object_detection/coin_cascade.xml')
goomba_cascade = cv2.CascadeClassifier('/home/logan/Projects/sm64_object_detection/goomba_cascade.xml')

cap = cv2.VideoCapture('/home/logan/Projects/sm64_object_detection/BBandWF.mp4')

fourcc = cv2.VideoWriter_fourcc(*'avc1') #(*'MP42')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mario = mario_cascade.detectMultiScale(gray,1.3,5)
        coins = coin_cascade.detectMultiScale(gray,1.1,5, minSize=(24,24), maxSize=(50,50))
        goombas = goomba_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in mario:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame, 'MARIO', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        for (x,y,w,h) in coins:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame, 'COIN', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        for (x,y,w,h) in goombas:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame, 'GOOMBA', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


        out.write(frame)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
