# 輸入金額與是否為會員
amount = float(input("請輸入購物總金額："))
is_member = input("是否為會員？(是/否)：")

# 將中文輸入轉為布林值
if is_member == "是":
    is_member = True
else:
    is_member = False

# 計算折扣
if amount > 500 and is_member:
    final_amount = amount * 0.8
elif amount > 500:
    final_amount = amount * 0.9
elif is_member:
    final_amount = amount * 0.95
else:
    final_amount = amount

# 四捨五入到整數
final_amount = round(final_amount)

# 輸出結果
print(f"折扣後金額為：{final_amount} 元")