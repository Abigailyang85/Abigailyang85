number_list = [-63, 43, -38, -90, -93, -87, 43, 52, 21, 80]

print(f"原本的排序: {number_list}")
print("")  # 分隔輸出用

number_list.sort()  # 直接修改原串列
print(f"sort_by_method 後的排序: {number_list}")
print("")  # 分隔輸出用

number_list.reverse()  # 直接修改原串列
print(f"reverse_by_method 後的排序: {number_list}")
print("")  # 分隔輸出用

new1_list = sorted(number_list, reverse=False)
print(f"新的串列：", new1_list)  # 新的串列
print(f"number_list 不變：", number_list)  # 排序沒變（已經被 .reverse()過後的排序）
print("")  # 分隔輸出用

new2_list = sorted(number_list, reverse=False)
print(f"新的串列：", new2_list)  # 新的串列
print(f"上面新的串列排序不變", new1_list)  # new1_list串列
print(f"number_list 不變：" ,number_list)  # 排序沒變（已經被 .reverse()過後的排序）
