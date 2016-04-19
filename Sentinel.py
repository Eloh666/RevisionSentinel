import xlrd
import smtplib
from datetime import datetime
from email import message

class DocScanner():
    def __init__(self, location):
        self.xlWorkbook = xlrd.open_workbook(location)
        self.xlSheet = self.xlWorkbook.sheet_by_index(0)

    def getRow(self, rowNumber):
        row = self.xlSheet.row(rowNumber)
        testDate = row[4]
        return  xlrd.xldate.xldate_as_datetime(testDate.value, self.xlWorkbook.datemode)

class MailSender():
    def __init__(self, message):
        self.message = message
        self.mail = smtplib.SMTP("smtp.gmail.com", 587)
        self.mail.ehlo()
        self.mail.starttls()
        self.mail.login("RevisionSentinel@gmail.com","revSentPass")

    def sendEmail(self):
        msg = message.Message()
        msg.add_header('from','Revision Sentinel')
        msg.add_header('to', 'davidemaurilio.morello@gmail.com')
        msg.add_header('subject', '__Agent__ REVISION due SOON')
        msg.set_payload(self.message)
        self.mail.sendmail("Revision Sentinel","davidemaurilio.morello@gmail.com",msg.as_string())

    def __exit__(self):
        self.mail.close()



test = MailSender("THIS IS A TEST MESSAGE")
test.sendEmail()
