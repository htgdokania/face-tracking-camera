import cv2
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'divx')
del_x=0
del_y=0
last_x=0
last_y=0
face_centre_x=0
face_centre_y=0
while True:
    ret,frame=cap.read()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640,480)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #detect face coordinates x,y,w,h
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    c=0
    for(x,y,w,h) in faces:
        c+=1
        if(c==1):
            face_centre_x=x+w/2
            face_centre_y=y+h/2
            del_x=last_x-320
            del_y=last_y-240
            last_x=face_centre_x
            last_y=face_centre_y
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),6)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
    cv2.imshow('frame',frame) #display image
    print('number of faces={}'.format(c))
    print('\ndel_x={}'.format(del_x))
    print('\ndel_y={}'.format(del_y))
    
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
