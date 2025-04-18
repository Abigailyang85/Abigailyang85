# 原始分數列表
scores = [85, 58, 90, 45, 70, 82, 60, 55]

# 設定及格線
pass_score = 60

# 分類及格與不及格
pass_scores = []
fail_scores = []
for score in scores:
    if score >= pass_score:
        pass_scores.append(score)
    else:
        fail_scores.append(score)

# 計算人數
num_pass = len(pass_scores)
num_fail = len(fail_scores)

# 輸出人數統計
print(f"及格人數：{num_pass} 人")
print(f"不及格人數：{num_fail} 人")

# Option：排序後輸出
print("及格分數（由高到低）：", sorted(pass_scores, reverse=True))
print("不及格分數（由低到高）：", sorted(fail_scores))