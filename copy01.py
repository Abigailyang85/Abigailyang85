# 假設有一個病患資料的串列：
patient_data_1 = [35, "男", [180, 75]]

#  patient_data_1 賦值給 patient_data_2
patient_data_2 = patient_data_1

# 現在兩個變數都指向同一個資料
patient_data_2[0] = 36  # 改變 age

# 由於 patient_data_1 和 patient_data_2 是同一個物件，修改後兩者都會改變
print(patient_data_1, "vs", patient_data_2)

# 使用 copy() 創建一個 shallow copy
import copy
patient_data_3 = copy.copy(patient_data_1)

# 修改shallow copy中的一個元素
patient_data_3[0] = 37  # 改變年齡

# 修改shallow copy的子串列的資料
patient_data_3[2][0] = 185  # 改變身高

# 可以看到，年齡變動不影響原資料，但身高變動影響了原資料
print(patient_data_1 , "vs",  patient_data_3)

# 使用 deepcopy() 創建一個 deep copy
patient_data_4 = copy.deepcopy(patient_data_1)

# 修改deep copy中的一個元素
patient_data_4[0] = 40  # 改變年齡

# 修改複製中的子串列的資料
patient_data_4[2][0] = 190  # 改變身高

# 可以看到，年齡變動和身高變動都不會影響原資料
print(patient_data_1 , "vs", patient_data_4)