#补充continue是跳过此次循环进行下一次，break是退出循环不再继续
"""
循环案例：发奖金
"""
money=10000

for i in range(1,21):
    import random
    score=random.randint(1,10)

    if score<5:
        print(f"员工{i}，绩效分{score}，低于5，不发奖金，下一位。")
        continue

    if money>=1000:
        money-=1000
        print(f"向员工{i}发工资1000元，账户余额还有{money}")
    else:
        print("奖金余额为0，绩效达标而未领取的，请明天再来。")
        break