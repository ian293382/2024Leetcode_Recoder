Score = [87, 66, 90, 65, 70]
Total_Score = 0
for i, e in enumerate(Score):
    print(f"第 {i+1} 位 的學生的分數: {e}")
    Total_Score += e  # 直接累加分数e
print(f"總分: {Total_Score}")
print(f"平均分: {Total_Score // len(Score)}")