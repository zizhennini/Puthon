grade_levels = {
    'A':range(90,101),
    'B':range(80,90),
    'C':range(70,80),
    'D':range(60,70),
    'E':range(0,60)
}

# 遍历字典，找到对应的等级
scores = [95,85,75,65,55]
for score in scores:
    for level,score_range in grade_levels.items():
        if score in score_range:
            print(f"成绩{score},等级：{level}")
