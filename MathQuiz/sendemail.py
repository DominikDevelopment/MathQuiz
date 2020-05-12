import questions
#import grade
import credentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#if grade.sendgrade == True: grade = str(grade.grade)



def makeemail():
    points = str(questions.points)
    name = str(questions.name)
    precentage = str(questions.precentage)

    email = credentials.email
    password = credentials.password
    send_to_email = credentials.email
    message = name + " got " + points + " that is " + precentage + "%"# + "We recommend giving him a " + grade

    msg = MIMEMultipart()
    msg['from'] = email
    msg['to'] = send_to_email
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
if questions.sendnow == True:
    #print(grade)
    makeemail()
