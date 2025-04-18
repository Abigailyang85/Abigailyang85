# 輸入格式：小時 (24小時制) 與是否為工作日
hour = int(input("請輸入出門時間（0-23的整數）："))
is_weekday = input("今天是工作日嗎？(是/否)：")

# 將中文輸入轉為布林值
if is_weekday == "是":
    is_weekday = True
else:
    is_weekday = False

# 決定交通工具
if is_weekday:
    if 7 <= hour <= 9:
        suggestion = "建議乘坐地鐵"
    elif 17 <= hour <= 19:
        suggestion = "建議走路或騎機車"
    else:
        suggestion = "建議開車"
else:
    suggestion = "建議騎自行車"

# 輸出建議
print(suggestion)