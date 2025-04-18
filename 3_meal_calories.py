# 輸入今日運動時間（單位：分鐘）與昨日攝入卡路里（單位：大卡）
exercise_minutes = int(input("請輸入今天運動的時間（分鐘）："))
yesterday_calories = int(input("請輸入昨天攝入的卡路里（大卡）："))

# 根據條件判斷今日建議攝入卡路里
if exercise_minutes > 60 and yesterday_calories < 2000:
    suggested_calories = 2500
elif exercise_minutes < 30:
    suggested_calories = 1500
else:
    suggested_calories = 2000

# 輸出建議
print(f"今天建議攝入：{suggested_calories} 大卡")