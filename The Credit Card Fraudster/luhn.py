last_number = 4

def luhn_check(num_arr):
    rev_num = num_arr[::-1]

    for i in range(len(rev_num)//2+1):
        rev_num[2*i] *= 2

    for i in range(len(rev_num)):
        if rev_num[i] > 9:
            rev_num[i] -= 9

    result  = sum(rev_num)
    result += last_number

    if result % 10 == 0:
        return True
    else :
        return False


for i in range(1000000):
    stars = f'{i:06d}'

    num_str = f'543210{stars}123'

    num_arr = [int(digit) for digit in num_str]

    print("현재 수 : " + num_str)

    if luhn_check(num_arr) == True:
        if int(num_str+'4') % 123457 == 0:
            print("정답")
            print(num_str)
            break

