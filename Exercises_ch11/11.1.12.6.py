from Exercises_ch11.SMS_store import SMS_store

my_inbox = SMS_store()

print(my_inbox.message_count())
my_inbox.add_new_arrival(1230, 12, "hoi")
print(my_inbox.message_count())