listSport=["爬山","游泳","跑步","舉重","飛輪","跳水","瑜珈"]
print(listSport[1:5])  #[1:5] 表示第2到第5個串列元素，顯示 ['游泳', '跑步', '舉重', '飛輪']
print(listSport[:4])   #[:4] 表示第1到第4個串列元素，顯示['爬山', '游泳', '跑步', '舉重']
print(listSport[1:6:2]) #[1:6:2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水'] 
print(listSport[6:1:-2])#[6:1:-2] 表示第7、5、3個串列元素，顯示['瑜珈', '飛輪', '跑步']
print(listSport[1::2])  #[1::2] 表示第2、4、6個串列元素，顯示['游泳', '舉重', '跳水']
