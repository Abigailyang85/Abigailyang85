# 1-100 之間用 range(1,101) 生成

for i in range(1, 101):
    if i % 4 == 0 and i % 7 == 0:
        print(i)
        break
