import random

#### https://wikidocs.net/94699
# lotto_num = []
# while len(lotto_num) != 6:
#     num = random.randint(1, 45)
#     if num not in lotto_num:
#         lotto_num.append(num)
# lotto_num_order = sorted(lotto_num)
# print(lotto_num_order)

####
#
button = 'y'
button = input("로또 번호를 생성하시겠습니가? (y/n) > ")
while True:
    if button == 'y' or 'yes' or 'Y':
        times = input("몇 번 하겠습니까? > ")

        lotto_num = []
        if times.isdigit():
            for i in range(len(times)):
                while len(lotto_num) != 6:
                    num = random.randint(1, 45)
                    if num not in lotto_num:
                        lotto_num.append(num)
                lotto_num_order = sorted(lotto_num)
                print(lotto_num_order)

    if button == 'n' or 'N' or 'NO' or 'no' or 'No':
        break


