import random

# 生成一個介於 0.0 到 1.0 之間的隨機浮點數
random_float = random.random()
print(random_float)

# 生成一個介於 1 和 10 之間（包括 1 和 10）的隨機整數
random_int = random.randint(1, 10)
print(random_int)

# 從非空序列中隨機選擇一個元素
sequence = ["apple", "banana", "cherry", "orange", "grape"]
random_choice = random.choice(sequence)
print(random_choice)

# 將序列中的元素隨機打亂
sequence_copy = sequence.copy()
random.shuffle(sequence_copy)
print(sequence)
print(sequence_copy)

# 從 population 中隨機選擇 k 個唯一元素，返回一個列表
population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_sample = random.sample(population, 3)
print(random_sample)

# 生成一個介於 start 和 stop 之間，步長為 step 的隨機整數
random_randrange = random.randrange(1, 10, 2)
print(random_randrange)

# 生成一個介於 a 和 b 之間的隨機浮點數
random_uniform = random.uniform(1.0, 10.0)
print(random_uniform)
