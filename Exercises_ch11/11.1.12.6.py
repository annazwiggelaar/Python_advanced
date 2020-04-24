from Exercises_ch11.SMS_store import SMS_store

my_inbox = SMS_store()

print(my_inbox.message_count())
my_inbox.add_new_arrival(1230, 12, "hoi")
my_inbox.add_new_arrival(1903, 13, "hallo")
print(my_inbox.message_count())

print(my_inbox.get_unread_indexes())
