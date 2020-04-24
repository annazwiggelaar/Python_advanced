class SMS_store:
    """Create new SMS store"""

    def __init__(self):
        self.sms_history = list()

    def __str__(self):
        text = ""
        for number, (_, from_number, time_arrived, text_of_SMS) in enumerate(self.sms_history):
            text += "{0}: {1} ({2})\n{3}\n".format(number, from_number, time_arrived, text_of_SMS)
        return text

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.sms_history.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.sms_history)

    def get_unread_indexes(self):
        unread = []
        for index, (read, _, _, _) in enumerate(self.sms_history):
            if not read:
                unread.append(index)
        return unread

    def get_message(self, index):
        _, from_number, time_arrived, text_of_SMS = self.sms_history[index]
        self.sms_history[index] = (True, from_number, time_arrived, text_of_SMS)
        return from_number, time_arrived, text_of_SMS

    def delete(self, index):
        self.sms_history.pop(index)

    def clear(self):
        self.sms_history = list()
