import cv2 
import imutils 

Nothing_in_frame = None
area = 500
frame = cv2.VideoCapture(0)

if not frame.isOpened():
    print("Cannot open camera")
    exit()

try:
   while True:
         _,img = frame.read()
         
         img = imutils.resize(img, width=1000)
         grayImg  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         blurredImg =cv2.GaussianBlur(grayImg, (21,21),0)
    
         if Nothing_in_frame is None:
             Nothing_in_frame = blurredImg
             continue

         DiffImg = cv2.absdiff(Nothing_in_frame, blurredImg)

         thresholdImg = cv2.threshold(DiffImg, 25, 255, cv2.THRESH_BINARY)[1]
         thresholdImg = cv2.dilate(thresholdImg, None, iterations=2)

         cnts = cv2.findContours(thresholdImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
         cnts=imutils.grab_contours(cnts)

         movement = False
         for c in cnts:
             if cv2.contourArea(c) < area:
                  
                  continue
             (x,y,w,h) = cv2.boundingRect(c)
             cv2.rectangle (img, (x,y), (x+w, y+h), (0,255,0),2)
            
             movement = True

         if movement:
            cv2.putText(img, "Movement Detected", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


         cv2.imshow("camera feed", img)
         if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
finally:
    frame.release()
    cv2.destroyAllWindows()