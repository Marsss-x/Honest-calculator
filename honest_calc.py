# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = float(0)
result = 0


def message(index_value):
    if index_value == 10:
        print(msg_10)
    elif index_value == 11:
        print(msg_11)
    else:
        if index_value == 12:
            print(msg_12)


def store():
    global memory
    global result
    while True:
        print(msg_4)
        y_n2 = input()
        if y_n2 == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    message(msg_index)
                    y_n3 = input()
                    if y_n3 == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            if msg_index == 12:
                                memory = result
                                return memory
                    elif y_n3 == 'n':
                        memory += 0
                        return memory
                    else:
                        if y_n3 != 'y' or 'n':
                            continue
            else:
                memory += result
                break
        elif y_n2 == 'n':
            memory += 0
            break
        else:
            if y_n2 != 'y' or 'n':
                continue


def is_one_digit(v):
    v = float(v)
    if -10.0 < v < 10.0 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    global msg_6
    global msg_7
    global msg_8
    global msg_9
    v1 = float(v1)
    v2 = float(v2)
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def calculator():
    global memory
    global result
    while True:
        print(msg_0)
        calc = input()
        try:
            x, oper, y = calc.split()
            if x == 'M':
                x = memory
            if y == 'M':
                y = memory
            elif y == 'M':
                y = memory
            x = float(x) or int(x) or str(x)
            y = float(y) or int(y) or str(y)
        except ValueError:
            print(msg_1)
        else:
            if oper == '+':
                check(x, y, oper)
                result = float(x) + float(y)
                print(result)
                return result
            elif oper == '-':
                check(x, y, oper)
                result = float(x) - float(y)
                print(result)
                return result
            elif oper == '*':
                check(x, y, oper)
                result = float(x) * float(y)
                print(result)
                return result
            elif oper == '/':
                check(x, y, oper)
                try:
                    float(x) / float(y)
                except ZeroDivisionError:
                    print(msg_3)
                else:
                    result = float(x) / float(y)
                    print(result)
                    return result
            else:
                if oper != ['+', '-', '*', '/']:
                    print(msg_2)


calculator()
store()
while True:
    print(msg_5)
    y_n = input()
    if y_n == 'n':
        break
    elif y_n == 'y':
        calculator()
        store()
    elif y_n != 'y' or 'n':
        continue
