import time

# 返回當前時間的時間戳（從新紀元到現在的秒數）
current_time_stamp = time.time()
print(f"time.time(): {current_time_stamp}")

# 讓程序暫停執行 2 秒
print("暫停 2 秒...")
# time.sleep(2)
print("繼續執行!")

# 返回當前本地時間的 struct_time 物件
local_time = time.localtime()
print(f"本機時間：{local_time}")

# 根據格式字符串 format 將時間 t 格式化為字符串
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(f"格式化時間： {formatted_time}")

# 根據格式字符串 format 將時間字符串 string 解析為 struct_time 物件
time_string = "2023-10-01 12:34:56"
time_format = "%Y-%m-%d %H:%M:%S"
parsed_time = time.strptime(time_string, time_format)
print(f"依照 {time_format} 將 {time_string} 轉換成 time 物件: {parsed_time}")

# time 物件的年月日時分秒
print(f"物件的年月日時分秒\n{local_time.tm_year}, {local_time.tm_mon}, {local_time.tm_mday}, {local_time.tm_hour}, {local_time.tm_min}, {local_time.tm_sec}")

# time 物件的星期，一年中的第幾天，夏令時間
print(f"物件的星期 {local_time.tm_wday}")
print(f"一年中的第幾天 {local_time.tm_yday}")
print(f"是否為夏令時間 {local_time.tm_isdst}")
