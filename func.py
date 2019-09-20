import random

def diceroll(cnt, max):
    num_list = []
    for i in range(0, cnt):
        num = random.randint(1, max)
        num_list.append(num)
    # サイコロの目の総和を計算しリストに入れる
    total = sum(num_list)
    num_list.append(total)
    return num_list