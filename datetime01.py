import datetime

current = datetime.datetime.now()：返回當前本地日期和時間。
datetime_format = "%Y-%m-%d %H:%M:%S"
print(f"格式化字串：{datetime.datetime.strftime(date_object, datetime_format)}")


datetime_string = "2025-04-10 15:30:30"
datetime_obj = datetime.datetime.strptime(datetime_string, datetime_format)
print(datetime_obj)
