import datetime

# 返回當前本地日期和時間。
current = datetime.datetime.now()
datetime_format = "%Y-%m-%d %H:%M:%S"
another_datetime_string = "2025-04-10 15:30:30"
another_datetime = datetime.datetime.strptime(another_datetime_string, datetime_format)


# 當前日期（物件）
current.date()
# 當前時間（物件）
current.time()
# 直接指定日期與時間
datetime_obj_1 = datetime.datetime(2024, 4, 1)
# 直接指定日期與時間
datetime_obj_2 = datetime.datetime(2024, 5, 1, 8, 10, 10)
# 計算日期差異
print(datetime_obj_1 - datetime_obj_2)
# 增加或減少時間
new_datetime_obj = current+ datetime.timedelta(weeks=1)
print(new_datetime_obj)
# 替換對應的時間屬性
replace_datetime = current.replace(year=2025, month=4, day=1, microsecond=0)
print(current)
print(replace_datetime)


from roc import ROCDate
rocdate = ROCDate(current)
print(rocdate.roc_year)
print(rocdate.month)
print(rocdate.day)
print(rocdate.hour)
print(rocdate.minute)
print(rocdate.second)
