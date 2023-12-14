class Time():
    def __init__ (self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__ (self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

    def __add__ (self, other):
        return Time(self.hour + other.hour, self.minute + other.minute, self.second + other.second)

    def __sub__ (self, other):
        return Time(self.hour - other.hour, self.minute - other.minute, self.second - other.second)

    def print(self):
        if self.hour < 10 and self.minute < 10 and self.second < 10:
            print("0" + str(self.hour) + ":0" + str(self.minute) + ":0" + str(self.second))
        elif self.hour < 10 and self.minute < 10:
            print("0" + str(self.hour) + ":0" + str(self.minute) + ":" + str(self.second))
        elif self.hour < 10 and self.second < 10:
            print("0" + str(self.hour) + ":" + str(self.minute) + ":0" + str(self.second))
        elif self.minute < 10 and self.second < 10:
            print(str(self.hour) + ":0" + str(self.minute) + ":0" + str(self.second))
        elif self.hour < 10:
            print("0" + str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))
        elif self.minute < 10:
            print(str(self.hour) + ":0" + str(self.minute) + ":" + str(self.second))

    def set(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def get(self):
        return self.hour, self.minute, self.second

time1 = Time(9, 30, 0)
time1.set(10, 30, 0)

time1.print()