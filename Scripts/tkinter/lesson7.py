
import cv2

# Capture video from file
cap = cv2.VideoCapture(1)

while True:

    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        print ('No')
        break

cap.release()
cv2.destroyAllWindows()