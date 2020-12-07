from winsound import Beep


class Note:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

    # Duration in miliseconds (ms, 1000ms = 1s)
    def beep(self, duration):
        Beep(self.frequency, duration)

    def __str__(self):
        return ("Name: {}, Frequency: {} Hz".format(self.name, self.frequency))
