import random


def sin():
    global limit
    global count
    if count < limit:
        choose = random.randint(0, 4)
    else:
        choose = random.randint(0, 3)
    body = ""
    if choose == 0:
        body = "sin(" + x() + ")"
    if choose == 1:
        body = "sin(" + cos() + ")"
    if choose == 2:
        body = "sin(" + num() + ")"
    if choose == 3:
        body = "sin(" + cos() + ")"
    if choose == 4:
        body = "sin((" + expr() + "))"

    choose = random.randint(-1000, 1000)
    if choose >= 0:
        body = body + "^  " + str(choose)

    return body


def cos():
    global limit
    global count
    if count < limit:
        choose = random.randint(0, 4)
    else:
        choose = random.randint(0, 3)
    body = ""
    if choose == 0:
        body = "cos(" + x() + ")"
    if choose == 1:
        body = "cos(" + cos() + ")"
    if choose == 2:
        body = "cos(" + num() + ")"
    if choose == 3:
        body = "cos(" + sin() + ")"
    if choose == 4:
        body = "cos((" + expr() + "))"

    choose = random.randint(-1000, 10000)
    if choose >= 0:
        body = body + "^  " + str(choose)

    return body


def x():
    choose = random.randint(-1000, 10000)

    if choose >= 0:
        return "x   ^  " + str(choose)
    else:
        return "x"


def num():
    choose = random.randint(0, 1000)
    sign = random.randint(0, 3)
    if sign == 0:
        return "+" + str(choose)
    if sign == 1:
        return "-" + str(choose)
    else:
        return str(choose)


def term():
    number = random.randint(1, 3)
    ans = ""

    choose = random.randint(0, 3)
    if choose == 0:
        ans += sin()
    if choose == 1:
        ans += cos()
    if choose == 2:
        ans += x()
    if choose == 3:
        ans += num()

    for i in range(number - 1) :
        choose = random.randint(0, 3)
        if choose == 0:
            ans += " *   " + sin()
        if choose == 1:
            ans += " *   " + cos()
        if choose == 2:
            ans += " *   " + x()
        if choose == 3:
            ans += " *   " + num()

    return ans


def expr():
    global count
    count += 1
    number = random.randint(1, 3)
    ans = term()

    for i in range(number):
        sign = random.randint(0, 1)
        if sign == 0:
            ans += " +  " + term()
        if sign == 1:
            ans += "    - " + term()
    return ans


limit = 1
count = 0
ans = expr()
print(ans)