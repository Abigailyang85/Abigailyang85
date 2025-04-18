# 原始食材清單
menu = ["雞肉", "吳郭魚", "青江菜", "花生", "洋蔥", "胡蘿蔔"]

# 晚上不想吃的食材（可以根據個人口味調整）
disliked_at_night = ["花生", "洋蔥"]

# 用 list comprehension 過濾掉不想吃的食材
dinner_menu = []
for item in menu:
    if item in disliked_at_night:
        continue
    dinner_menu.append(item)


# 輸出結果
print("晚餐用的食材清單：")
print(dinner_menu)