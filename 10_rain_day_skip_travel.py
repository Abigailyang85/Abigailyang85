sights = ["博物館", "公園", "古蹟", "購物中心", "美食街", "動物園", "遊樂園"]
weather = ["晴天", "雨天", "雨天", "晴天", "雨天", "晴天", "晴天"]

print("開始本次參觀行程...")

for i in range(len(sights)):
    current_weather = weather[i]
    current_sight = sights[i]
    
    if current_weather == "雨天":
        print(f"現在天氣{current_weather}，跳過「{current_sight}」的行程，等待天氣轉好。")
        continue
    
    print(f"現在天氣是{current_weather}，參觀「{current_sight}」。")
    
    # 是否想要繼續旅程
    choice = input("是否繼續旅遊？(y/n)：")
    if choice.lower() == "n":
        break

print("結束旅程！")