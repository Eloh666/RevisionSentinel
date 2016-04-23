import smtplib
from email import message

class MailSender():
    def __init__(self):
        self.mail = smtplib.SMTP("smtp.gmail.com", 587)
        self.mail.ehlo()
        self.mail.starttls()
        self.mail.login("RevisionSentinel@gmail.com","revSentPass")

    def sendEmail(self, agent, days, body, recipient):
        msg = message.Message()
        msg.add_header('from','Revision Watcher')
        msg.add_header('to', 'davidemaurilio.morello@gmail.com')
        temp = "REMINDER: "+agent+" revision due in "+ days + "days!"
        msg.add_header('subject', str(temp))
        msg.set_payload(body)
        self.mail.sendmail("Revision Sentinel",recipient, msg.as_string())

    def __exit__(self):
        self.mail.close()