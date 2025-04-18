text = "鋼彈吊單槓"
text2 = "今天去練習了吊單槓，我超累的"
text3 = "Chinese Culture University."
print(text.center(20, "="))  # 使字串居中對齊，字串總長度擴充到20
print(text2.find("吊單槓"))  # 查找 "吊單槓" 出現的位置，若未找到返回 -1
print(text2.find("爺爺"))  # 查找 "吊單槓" 出現的位置，若未找到返回 -1
print(text2.endswith("的"))  # 判斷字串是否以 "的" 結尾
print("鋼彈".islower())  # 判斷字串是否全部是小寫字母
print("鋼彈".isupper())  # 判斷字串是否全部是大寫字母
words = ["今天", "去", "練習", "吊單槓"]
print(" ".join(words))  # 用空格將列表中的字串連接起來
print(",".join(words))  # 用,將列表中的字串連接起來
print(";".join(words))  # 用;將列表中的字串連接起來
print(len(text))  # 輸出字串的長度
print(text.ljust(20, "*"))  # 將字串左對齊，並用 '*' 填充右側，總長度為20
print(text3.lower())  # 將字串轉換為小寫
print("   鋼彈吊單槓".lstrip())  # 去除字串開頭的空白字符
print(text2.replace("吊單槓", "引體向上"))  # 將 "吊單槓" 替換為 "引體向上"
print(text.rjust(20, "-"))  # 將字串右對齊，並用 "-" 填充左側，總長度為20
print("鋼彈吊單槓---".rstrip("-"))  # 去除字串結尾的空白字符
print(text2.split("吊單槓"))  # 根據 "吊單槓" 將字串分割成列表
print(text2.startswith("今天"))  # 判斷字串是否以 "今天" 開頭
print("   鋼彈吊單槓   ".strip())  # 去除字串兩側的空白字符
print(text3.upper())  # 將字串轉換為大寫
