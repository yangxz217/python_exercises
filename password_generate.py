import random

# 字符集
digital = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cLetter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*']


# 初始化结果
def init_result():
    result = str()
    return result


# 初始化长度
def init_length():
    length = int(input("请输入密码长度(6-32)："))
    return length


# 初始化组成成分
def init_comp():
    comp = int(input("请输入参数(1：数字，2：小写字母，3：数字与小写字母，4：数字与字母，5：数字小写字母特殊符号，6：数字字母与特殊符号)\n："))
    return comp


# 主函数
def password_generator():
    result = init_result()
    length = judge_length()
    judge_comp(init_comp(), length, result)


# 判断长度
def judge_length():
    length = init_length()
    while length < 6 or length > 32:
        if length < 6:
            print("密码长度太短！")
            length = init_length()
        elif length > 32:
            print("密码长度太长！")
            length = init_length()
        else:
            break
    return length


# 判断组成成分
def judge_comp(comp, length, result):
    if comp == 1:
        only_digital(length, result)
    elif comp == 2:
        only_lower_letter(length, result)
    elif comp == 3:
        digital_lower_letter(length, result)
    elif comp == 4:
        digital_letters(length, result)
    elif comp == 5:
        digital_lower_letter_symbol(length, result)
    elif comp == 6:
        digital_letters_symbol(length, result)
    else:
        print("参数错误，请重新输入!")
        judge_comp(init_comp(), length, result)


# 密码由纯数字组成
def only_digital(length, result):
    for i in range(length):
        result += random.choice(digital)
    print("密码是:"+result+"\n")


# 密码由小写字母组成
def only_lower_letter(length, result):
    for i in range(length):
        result += random.choice(lLetter)
    print("密码是:"+result+"\n")


# 密码由数字，小写字母组成
def digital_lower_letter(length, result):
    for i in range(length):
        kind = random.randint(1, 2)
        if kind == 1:
            result += random.choice(digital)
        else:
            result += random.choice(lLetter)
    print("密码是:"+result+"\n")


# 密码由数字，字母组成
def digital_letters(length, result):
    for i in range(length):
        kind = random.randint(1, 3)
        if kind == 1:
            result += random.choice(digital)
        elif kind == 2:
            result += random.choice(lLetter)
        else:
            result += random.choice(cLetter)
    print("密码是:"+result+"\n")


# 密码由数字，小写字母，特殊符号组成
def digital_lower_letter_symbol(length, result):
    for i in range(length):
        kind = random.randint(1, 3)
        if kind == 1:
            result += random.choice(digital)
        elif kind == 2:
            result += random.choice(lLetter)
        else:
            result += random.choice(symbol)
    print("密码是:"+result+"\n")


# 密码由数字，字母，特殊符号组成
def digital_letters_symbol(length, result):
    for i in range(length):
        kind = random.randint(1, 4)
        if kind == 1:
            result += random.choice(digital)
        elif kind == 2:
            result += random.choice(lLetter)
        elif kind == 3:
            result += random.choice(cLetter)
        else:
            result += random.choice(symbol)
    print("密码是:"+result+"\n")


if __name__ == '__main__':
    password_generator()
