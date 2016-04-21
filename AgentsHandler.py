import xlrd
import datetime

class DocScanner():
    def __init__(self, location):
        self.xlWorkbook = xlrd.open_workbook(location)
        self.xlSheet = self.xlWorkbook.sheet_by_index(0)
        self.now = datetime.datetime.now()

    def checkAgents(self):
        allAgents = []
        for i in range(1, self.xlSheet.nrows):
            row = self.xlSheet.row(i)
            revisionDate = row[4]
            revisionDate = xlrd.xldate.xldate_as_datetime(revisionDate.value, self.xlWorkbook.datemode)
            timeDelta = revisionDate - self.now
            allAgents.append((row[1].value+" "+row[2].value, row[3].value, str(revisionDate).replace(" 00:00:00",""), timeDelta.days, row[5].value ))
        return allAgents
