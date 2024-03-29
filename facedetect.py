import cv2

cap = cv2.VideoCapture(cv2.CAP_DSHOW)
new_path = 'C:/Users/DELL/Anaconda3/Library/etc/haarcascades/'

face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_frontalface_default.xml')

while True:
	ret,frame = cap.read()

   
	if ret == False:
		continue
	faces = face_cascade.detectMultiScale(frame,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow("Video Frame",frame)
	

	#Wait for user input - q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break


cap.release()
cv2.destroyALlWindows()