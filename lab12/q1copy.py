from calendar import month
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from bookinglist import Ui_Form as BookingListForm
from selectbooking import Ui_Form as SelectBookingForm
from PySide6.QtGui import QStandardItem, QStandardItemModel

class BookingApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = BookingListForm()
        self.ui.setupUi(self)
        print(year, month, day)
        Bookinglist = ui1.listBookings(Date(year, month, day))
        print(Bookinglist)
        # print(date)
        # format [(datetime.date(2011, 10, 1), ['Booking#2', 'Booking#3'])]
        # add booking1 and booking2 to the listView
        
        model = QStandardItemModel()
        for date, bookings in Bookinglist:
            for booking in bookings:
                item = QStandardItem(f"{date} : {booking}")
                model.appendRow(item)
        
        self.ui.listView.setModel(model)


from datetime import date as Date



class BookingApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = BookingListForm()
        self.ui.setupUi(self)
        print(year, month, day)
        Bookinglist = ui1.listBookings(Date(year, month, day))
        print(Bookinglist)
        # print(date)
        # format [(datetime.date(2011, 10, 1), ['Booking#2', 'Booking#3'])]
        # add booking1 and booking2 to the listView
        model = QStandardItemModel()
        for date, bookings in Bookinglist:
            for booking in bookings:
                item = QStandardItem(f"{date} : {booking}")
                model.appendRow(item)
        
        self.ui.listView.setModel(model)




        # connect the buttons (name pushButton)
        self.ui.pushButton.clicked.connect(self.showSelectBooking)

        # update the viewList based on the date
    


        # print(date)




    def showSelectBooking(self):
        # close the current window
        self.close()
        self.selectBooking = SelectBookingPage()
        self.selectBooking.show()



class SelectBookingPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = SelectBookingForm()
        self.ui.setupUi(self)

        # connect the buttons (name pushButton)
        self.ui.pushButton.clicked.connect(self.showBookingList)


    def showBookingList(self):
        global year, month, day
        year = int(self.ui.textEdit_3.toPlainText())
        month = int(self.ui.textEdit_2.toPlainText())
        day = int(self.ui.textEdit.toPlainText())
        # print(year, month, day)
        date = Date(year, month, day)
        ui1.submit(date)
        # print everything in the object
        # print(s.bookings)
        self.close()
        self.bookingList = BookingApp()
        self.bookingList.show()

class BookingSystem(object):
    def __init__(self):
        self.observers = []
        self.bookings = {}

    def addObserver(self, o):
        self.observers.append(o)

    def notifyObservers(self, booking):
        for o in self.observers:
            o.update(booking)

    def addBooking(self, date, booking):
        if date in self.bookings:
            self.bookings[date].append(booking)
        else:
            self.bookings[date] = [booking]
        
    def getBookings(self, date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append((k, v))

        self.notifyObservers(bookings)
        return bookings

    def display(self, date):
        self.getBookings(date)

class BookingObserver(object):
    def update(self, data):
        pass

class StaffUi(BookingObserver):
    def __init__(self,s,name):
        self.name = name
        self.system = s
    
    def update(self, bookings):
        print(self.name + ": StaffUi.update() :")
        print("-- Booking Data --")
        for data in bookings:
            items = data[1]
            for item in items:
                print(str(data[0]) + " : " + item)

    def listBookings(self, date):
        return self.system.getBookings(date)

    def submit(self, date):
        self.system.display(date)



# s = BookingSystem()


# ui1 = StaffUi(s, "UI#1")
# s.addObserver(ui1)


# ui1.submit(Date(2011, 10, 1))

if __name__ == "__main__":
    year = 2011
    month = 10
    day = 1
    
    app = QApplication([])
    s = BookingSystem()
    
    s.addBooking(Date(2011, 9, 1), "Booking#1")
    s.addBooking(Date(2011, 10, 1), "Booking#2")
    s.addBooking(Date(2011, 10, 1), "Booking#3")
    s.addBooking(Date(2011, 11, 1), "Booking#4")
    s.addBooking(Date(2011, 12, 1), "Booking#5")

    ui1 = StaffUi(s, "UI#1")
    s.addObserver(ui1)

    # ui1.submit(Date(2011, 10, 1))
    # ui1.submit(Date(2011, 11, 1))
    date = Date(2011, 10, 1)
    window = BookingApp()
    window.show()

    app.exec()


