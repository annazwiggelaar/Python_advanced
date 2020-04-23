class SMS_store:
    """Create new SMS store"""

    def __init__(self):
        self.sms_history = list()

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.sms_history.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.sms_history)

    def get_unread_indexes(self):
        for messages in self.sms_history:
            if self.sms_history.index(self) is False:
            return

    def get_message(self, i):
        i = input(int("Which message do you want to see? Please provide a number."))
        message = self.sms_history.index(i)
        return message



