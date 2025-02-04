import jdatetime

now = jdatetime.datetime.now()
# minute = now.strftime("%M")
# hour = now.strftime("%H")
minute = now.minute
hour = now.hour
print(hour)
print(type(minute))
