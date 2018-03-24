import sched, time
import csv
from newsPaperRecord import NewsPaperRecord as NewPaperRecord
from multiprocessing import Queue
from estractor import getPageFromLink

s = sched.scheduler(time.time, time.sleep)
newPapersQueue = Queue(maxsize=0)


def getUpNewPapers():
    with open('periodicos.csv', 'rb') as csvfile:
        newPapers = csv.reader(csvfile)
        for row in newPapers:
            country =  unicode(row[0], "utf-8")
            name = row[1]
            link = row[2]
            newPapersQueue.put(NewPaperRecord(country,name,link))

def do_something(sc):
    print "Search newPaper page..."
    aNewsPaperRecord = newPapersQueue.get()
    print aNewsPaperRecord.name
    getPageFromLink(aNewsPaperRecord.link)
    s.enter(10, 1, do_something, (sc,))



getUpNewPapers()
s.enter(60, 1, do_something, (s,))
s.run()