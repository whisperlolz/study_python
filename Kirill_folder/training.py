# If approach
# count_positive = 0
# count_negative = 0
# max_num = None
# min_num = None
# sum_num = 0
#
# while True:
#     num = int(input("Wprowadz liczbe: "))
#
#     if num != 0:
#
#         if num > 0:
#             count_positive += 1
#         if num < 0:
#             count_negative += 1
#
#         if max_num is None or min_num is None:
#             max_num = num
#             min_num = num
#
#         if max_num < num:
#             max_num = num
#
#         if min_num > num and min_num != 0:
#             min_num = num
#
#         sum_num += num
#
#     if num == 0:
#
#         if count_positive == 0 and count_negative == 0:
#             print("Brak liczb")
#             break
#
#         else:
#             print(f"""
# >0: {count_positive}
# <0: {count_negative}
# min: {min_num}
# max: {max_num}
# sum: {sum_num}
# count: {count_positive + count_negative}
# avg: {round(sum_num / (count_positive + count_negative), 2)}""")
#         break

# List approach
nums_list = []
count_positive = 0
count_negative = 0

while True:
    try:
        ask_num = int(input("Wprowadz liczbe: "))
        if ask_num != 0:
            nums_list.append(ask_num)
            if ask_num > 0: count_positive += 1
            if ask_num < 0: count_negative += 1
        if ask_num == 0:
            if len(nums_list) > 0:
                print(f"""
list: {nums_list}
>0: {count_positive}
<0: {count_negative}
min: {min(nums_list)}
max: {max(nums_list)}
sum: {sum(nums_list)}
count: {len(nums_list)}
avg: {round(sum(nums_list) / len(nums_list), 2)}""")
                break
            else:
                print("Nie masz nic do podliczenia!")
                break
    except ValueError:
        print("Musisz podac liczbe!")
