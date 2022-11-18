# import cv2
# import numpy as np
# import smtplib
# import threading
# from playsound import playsound
# #test 

# Alarm_Status = False
# Email_Status = False
# Fire_Reported = 0

# def play_alarm_sound_function():
# 	while True:
# 		playsound('Alarm Sound.mp3',True)

# def send_mail_function():

#     recipientEmail = ""
#     recipientEmail = recipientEmail.lower()

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login("nguyennga16062000@gmail.com", '16062000')
#         server.sendmail('nguyennga1606ictbk@gmail.com', recipientEmail, "Warning A Fire Accident has been reported on ABC Company")
#         print("sent to {}".format(recipientEmail))
#         server.close()
#     except Exception as e:
#     	print(e) 
     
  
# if __name__ == "__main__":
#     video = cv2.VideoCapture("Fire.mp4") 
    
#     while True:
#         (grabbed, frame) = video.read()
#         if not grabbed:
#             break

#         frame = cv2.resize(frame, (960, 540)) 
    
#         blur = cv2.GaussianBlur(frame, (15, 15), 0)
#         hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
#         lower = [18, 50, 50]
#         upper = [35, 255, 255]
#         lower = np.array(lower, dtype="uint8")
#         upper = np.array(upper, dtype="uint8")

#         mask = cv2.inRange(hsv, lower, upper)
    
#         output = cv2.bitwise_and(frame, hsv, mask=mask)

#         number_of_total = cv2.countNonZero(mask)
        
#         no_red = cv2.countNonZero(mask)

#         if int(no_red) > 15000:
#             Fire_Reported = Fire_Reported + 1

#         cv2.imshow("output", output)
#         threads = []

#         if Fire_Reported >= 1:
#             if Alarm_Status == False:
#                 threading.Thread(target=play_alarm_sound_function).start()
#                 Alarm_Status = True

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cv2.destroyAllWindows()
#     video.release()


import cv2
import numpy as np
import smtplib
import playsound
import threading

Alarm_Status = False
Email_Status = False
Fire_Reported = 0

def play_alarm_sound_function():
	while True:
		playsound.playsound('Alarm Sound.mp3',True)

def send_mail_function():

    recipientEmail = "nguyennga1606ictbk@gmail.com"
    recipientEmail = recipientEmail.lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("nguyennga16062000@gmail.com", 'zoboqlrtgczwxmsz')
        server.sendmail('nguyennga1606ictbk@gmail.com', recipientEmail, "SOS, Thong bao co dam chay tai dia diem X")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
    	print(e)


video = cv2.VideoCapture("Fire.mp4") # If you want to use webcam use Index like 0,1.

while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    frame = cv2.resize(frame, (960, 540))

    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)

    no_red = cv2.countNonZero(mask)

    if int(no_red) > 1500:
        Fire_Reported = Fire_Reported + 1

    cv2.imshow("output", output)

    if Fire_Reported >= 1:
        if Alarm_Status == False:
            threading.Thread(target=play_alarm_sound_function).start()
            Alarm_Status = True
        if Email_Status == False:
            threading.Thread(target=send_mail_function).start()
            Email_Status = True
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
video.release()