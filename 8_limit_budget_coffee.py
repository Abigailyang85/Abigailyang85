# 咖啡價目表
coffee_menu = {
    "香草拿鐵": 75,
    "美式咖啡": 50,
    "拿鐵咖啡": 60,
    "卡布奇諾": 60,
    "摩卡咖啡": 70
}

# 初始預算
budget = 200
total_spent = 0
cups = []
remaining = budget

# 嘗試依序點每種咖啡直到預算用完
for coffee, price in coffee_menu.items():
    if remaining >= price:
        cups.append(coffee)
        total_spent += price
        remaining -= price
    else:
        break  # 錢不夠了，停止點餐

# 結果輸出
print("你點了以下咖啡：")
for coffee in cups:
    print(f"- {coffee}：{coffee_menu[coffee]} 元")

print(f"\n總共點了 {len(cups)} 杯咖啡")
print(f"總共花了 {total_spent} 元")
print(f"預算剩下 {remaining} 元")