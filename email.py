import smtplib

import time

import datetime

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from email.mime.application import MIMEApplication


#pip install twillio

from twilio.rest import Client


account_sid = 'AC00394fc838ee445cd0dc9073eea7d739'

auth_token = '20a9e1975747429097a2717860a6a6ea'

client = Client(account_sid, auth_token)




def record():

with picamera.Picamera() as camera:

camera.resolution = (640, 480)

cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

file_name = cur_time + '.h264'

camera.start_recording(file_name)

camera.wait_recording(10)

camera.stop_recording()

return file_name








def send_mail(send_file):


smtp= smtplib.SMTP('smtp.gmail.com',587)

smtp.starttls()

smtp.login('sprpsa9702@gmail.com','gcvcstkrylxjucol')

msg=MIMEMultipart()

msg['Subject']='방문자가 있습니다.'

msg['To']='sprpsa33@naver.com'

text=MIMEText('외부인이 출입하였습니다')

msg.attach(text)

with open(send_file,'rb') as file_FD:

etcPart = MIMEApplication(file_FD.read())


#MIME 헤더에 첨부파일의 정보추가

etcPart.add_header('COntent-Disposition','attachment', filename=send_file)

msg.attach(etcPart)

smtp.sendmail('sprpsa9702@gmail.com','sprpsa33@naver.com', msg.as_string())

smtp.quit()








def send_sms():

message = client.messages.create(

body='방문자가 있습니다. 메일을 확인하세요',

from_='+15134502503',

to='+821087226197')







def 얼굴인식하면 :


send_file = record()

cur_time=time.strftime('%Y-%m-%d%H:%M',time.localtime(time.time()))

title='방문자가 있습니다.'

send_mail(title,cur_time+'자료입니다.','sprpsa33@naver.com',send_file)

send_sms(title,'+821087226197')