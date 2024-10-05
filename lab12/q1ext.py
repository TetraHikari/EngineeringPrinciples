import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from bookinglist import Ui_Form as BookingListForm
from selectbooking import Ui_Form as SelectBookingForm


class BookingSystem(QObject):
    def __init__(self):
        super().__init__()
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


class BookingObserver(QObject):
    def update(self, data):
        pass


class StaffUi(BookingObserver):
    def __init__(self, s, name):
        super().__init__()
        self.name = name
        self.system = s

    def update(self, bookings):
        print(self.name + ": StaffUi.update() :")
        print("-- Booking Data --")
        for data in bookings:
            items = data[1]
            for item in items:
                print(str(data[0]) + " : " + item)

    def submit(self, date):
        self.system.display(date)


class BookingList(QWidget, BookingListForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SelectBooking(QWidget, SelectBookingForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # s = BookingSystem()
    # s.addBooking(QDate(2011, 9, 1), "Booking#1")
    # s.addBooking(QDate(2011, 10, 1), "Booking#2")
    # s.addBooking(QDate(2011, 10, 1), "Booking#3")
    # s.addBooking(QDate(2011, 11, 1), "Booking#4")
    # s.addBooking(QDate(2011, 12, 1), "Booking#5")

    # ui1 = StaffUi(s, "UI#1")
    # s.addObserver(ui1)

    # ui1.submit(QDate(2011, 10, 1))

    # Create and show the main window
    booking_list_window = BookingList()
    booking_list_window.show()

    sys.exit(app.exec())

