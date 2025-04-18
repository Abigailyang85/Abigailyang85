# 每日旅行花費資料
daily_expenses = {
    "週一": 300,
    "週二": 500,
    "週三": 400,
    "週四": 200,
    "週五": 700,
    "週六": 800,
    "週日": 350
}

# 計算總花費與平均花費
total_expense = sum(daily_expenses.values())
average_expense = total_expense / len(daily_expenses)

# 找出最花錢與最省錢的一天

max_expense = 0
max_day = None
min_expense = max(daily_expenses.values())
min_day = None
for weekday, expense in daily_expenses.items():

    if expense > max_expense:
        max_expense = expense
        max_day = weekday

    if expense < min_expense:
        min_expense = expense
        min_day = weekday

# 輸出結果
print(f"總花費：{total_expense} 元")
print(f"平均花費：{round(average_expense, 2)} 元")
print(f"最花錢的一天是 {max_day}，花了 {max_expense} 元")
print(f"最省錢的一天是 {min_day}，花了 {min_expense} 元")