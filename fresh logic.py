import serial                                 # add Serial library for Serial communication
import cv2

Arduino_Serial = serial.Serial('com10',9600)  #Create Serial port object called arduinoSerialData
print Arduino_Serial.readline()               #read the serial data and print it as line
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(1)
fourcc=cv2.VideoWriter_fourcc(*'divx')
pix_move_x=0
pix_move_y=0
face_change_x=0
face_change_y=0
changex=0
changey=0

while True:
    pix_move_x=0
    pix_move_y=0
    changex=0
    changey=0
    ret,frame=cap.read()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640,480)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    
    #detect face coordinates x,y,w,h
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    c=0
    for(x,y,w,h) in faces:
        c+=1
        #centre of face
        face_centre_x=x+w/2
        face_centre_y=y+h/2
        #pixels to move 
        pix_move_x=320-face_centre_x
        pix_move_y=240-face_centre_y
        #convert pixel to angle where angle may vary from -90 to +90
        changex=(pix_move_x*9)/32
        changey=(pix_move_y*9)/24
        if(c==1):
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),6)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
    cv2.imshow('frame',frame) #display image
    print("pix_x={}".format(pix_move_x))
    print("pix_y={}".format(pix_move_y))
    print("changex={}".format(changex))
    #divide the obtained angle to convert in an
    #integer from 1-9 to send to the arduino    
    changex/=10
    changey/=10
    
##    if(changex<0):
##        Arduino_Serial.write('-')
##        changex*=-1

    print("changex={}".format(changex))
    
    Arduino_Serial.write(changex)
    
    print Arduino_Serial.readline()               #read the serial data and print it as line

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
