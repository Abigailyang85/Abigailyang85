import datetime
import pytz

tzinfo = pytz.timezone("Asia/Taipei")
current_datetime = datetime.datetime.now(tzinfo)

print(current_datetime.strftime("%Y %m %d %H %M %S %f"))
print(current_datetime.strftime("%Y %m %d %H %M %S %Z"))
print(current_datetime.strftime("%Y %m %d %H %M %S %z"))
print(current_datetime.strftime("%Y %m(%b) %d %A(%a)"))
print(current_datetime.strftime("%H(%p %h) %M %S"))
