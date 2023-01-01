import smtplib
from email.message import EmailMessage



class Email_msg:
    def __init__(self,subject,body,to):
        self.subject=subject
        self.body=body
        self.to=to
        pass

    def email_msg(self):
        
        try:
            msg=EmailMessage()
            msg.set_content(self.body)
            msg['subject']=self.subject
            msg['to']=self.to

            user="adityarokade76@gmail.com"
            msg['from']=user
            password="wmsethxsydonmdsp"

            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
            server.quit()
        except:
            print("Error in sending email-notification ")
