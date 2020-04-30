class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs"""
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def __str__(self):
        return "({0}:{1}:{2})".format(self.hours, self.minutes, self.seconds)

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

        return self.hours, self.minutes, self.seconds

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

