import random

digital = ['0','1','2','3','4','5','6','7','8','9']
lLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
cLetter = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol = ['!','@','#','$','%','^','&','*']

def initResult():
    result = str()
    return result

def initLength():
    length = int(input("请输入密码长度(6-32)："))
    return length

def initComp():
    comp = int(input("请输入参数(1：数字，2：小写字母，3：数字与小写字母，4：数字与字母，5：数字小写字母特殊符号，6：数字字母与特殊符号)\n："))
    return comp

def password_generator():
    result = initResult()
    length = judgeLength()
    judgeComp(initComp(), length, result)

def judgeLength():
    length = initLength()
    while length < 6 or length > 32:
        if length < 6:
            print("密码长度太短！")
            length = initLength()
        elif length > 32:
            print("密码长度太长！")
            length = initLength()
        else:
            break
    return length
    
def judgeComp(comp, length, result):
    if comp == 1:
        result = onlyDigital(length, result)
    elif comp == 2:
        result = onlyLletter(length, result)
    elif comp == 3:
        result = digitalAndLletter(length, result)
    elif comp == 4:
        result = digitalAndLetters(length, result)
    elif comp == 5:
        result = digitalLletterAndSymbol(length, result)
    elif comp == 6:
        result = digitalLettersAndSymbol(length, result)
    else:
        print("参数错误，请重新输入!")
        judgeComp(initComp(), length, result)

def onlyDigital(length, result):
    for i in range(length):
        result += random.choice(digital)
    print("密码是:"+result+"\n")

def onlyLletter(length, result):
    for i in range(length):
        result += random.choice(lLetter)
    print("密码是:"+result+"\n")

def digitalAndLletter(length, result):
    for i in range(length):
        kind = random.randint(1, 2)
        if kind == 1:
            result += random.choice(digital)
        else:
            result += random.choice(lLetter)
    print("密码是:"+result+"\n")


def digitalAndLetters(length, result):
    for i in range(length):
        kind = random.randint(1, 3)
        if kind == 1:
            result += random.choice(digital)
        elif kind == 2:
            result += random.choice(lLetter)
        else:
            result += random.choice(cLetter)
    print("密码是:"+result+"\n")

def digitalLletterAndSymbol(length, result):
    for i in range(length):
        kind = random.randint(1, 3)
        if kind == 1:
            result += random.choice(digital)
        elif kind == 2:
            result += random.choice(lLetter)
        else:
            result += random.choice(symbol)
    print("密码是:"+result+"\n")

def digitalLettersAndSymbol(length, result):
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

password_generator()