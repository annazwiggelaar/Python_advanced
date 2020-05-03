class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs"""
        total_secs = hrs * 3600 + mins * 60 + secs
        self.hours = total_secs // 3600
        leftover_secs = total_secs % 3600
        self.minutes = leftover_secs // 60
        self.seconds = leftover_secs % 60

    def __str__(self):
        return "({0}:{1}:{2})".format(self.hours, self.minutes, self.seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def increment(self, seconds):
        added = self.to_seconds() + seconds
        return MyTime(0, 0, added)

    def add_time(self, t2):
        secs = self.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)

    def after(self, t2):
        return self.to_seconds() > t2.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def between(self, t1, t2):
        if t1.to_seconds() <= self.to_seconds() < t2.to_seconds():
            return True



