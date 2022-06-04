def circle(data_string):
    if data_string[0] == '(':
        data_string = data_string[1:]
        result = form(data_string)
        if result[0] != ')':
            return '-'
        result = result[1:]
        return form(result)
    else:
        return data_string


def square(data_string):

    if data_string[0] == '[':
        data_string = data_string[1:]
        result = circle(data_string)
        if result[0] != ']':
            return '-'
        result = result[1:]
        return form(result)
    else:
        return data_string


def figure(data_string):
    if data_string[0] == '{':
        data_string = data_string[1:]
        result = circle(data_string)
        if result[0] != '}':
            return '-'
        result = result[1:]
        return form(result)
    else:
        return data_string


def form(data_string):
    result = data_string

    if data_string[0] == '(':
        result = circle(data_string)
    elif data_string[0] == '[':
        result = square(data_string)
    elif data_string[0] == '{':
        result = figure(data_string)

    return result


def start(data_string):
    data_string += '#'

    result = form(data_string)
    if result == '#':
        print("Введена правильная скобочная запись.")
    else:
        print("Введена неправильная скобочная запись.")


print("\nПравильная скобочная запись с тремя видами скобок."
      "\nВнутри фигурных и квадратных скобок могут быть только круглые, внутри круглых любые.")

while True:
    print("\nВведите скобочную последовательность:"
          "\n(Для выхода из программы введите '0')")
    input_string = input()

    if input_string == '0':
        break

    start(input_string)
