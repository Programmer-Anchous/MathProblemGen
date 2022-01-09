import random


# Функция "find_nums" ищет начало и конец всех чисел в строке, пример работы:
# Ввод: "123 + 4 * 34"
# Вывод: [[0, 3], [6, 7], [10, 12]]
def find_nums(problem) -> list:
    if len(problem) == 1:
        return [[0, 1]]
    nums_in_str = []
    flag = False

    for i in range(len(problem)):
        if not flag and problem[i].isdigit():
            nums_in_str.append([i])
            flag = True

        elif flag and (not problem[i].isdigit() or i == len(problem)):
            nums_in_str[-1].append(i)
            flag = False
    nums_in_str[-1].append(len(problem))
    return nums_in_str


# Функция "amount" заменяет число суммой двух других чисел, пример работы:
# Ввод: 12
# Вывод: 5 + 7
def amount(num, problem) -> str:
    if num > 1:
        num1 = random.randrange(1, num)
        num2 = num - num1
        return f"({num1} + {num2})"
    return num


# Функция "difference" заменяет число разностью двух других чисел, пример работы:
# Ввод: 12
# Вывод: 20 - 8
def difference(num, problem) -> str:
    num1 = random.randrange(num + 1, num * 3)
    num2 = num1 - num
    return f"({num1} - {num2})"


# Функция "multiplication" заменяет число произведением двух других чисел, пример работы:
# Ввод: 12
# Вывод: 3 × 4
def multiplication(num, problem) -> str:
    divisors = [(int(num / i), i) for i in range(2, num) if num % i == 0]
    if divisors:
        terms = random.choice(divisors)
        if "÷" not in problem and "×" not in problem:  # если в строке нет умножения или деления скобки не нужны
            return f"{terms[0]} × {terms[1]}"
        return f"({terms[0]} × {terms[1]})"
    return num


# Функция "division" заменяет число деленим двух других чисел, пример работы:
# Ввод: 12
# Вывод: 36 ÷ 3
def division(num, problem) -> str:
    num1 = random.randrange(2, 11)
    if "÷" not in problem and "×" not in problem:  # если в строке нет умножения или деления скобки не нужны
        return f"{num * num1} ÷ {num1}"
    return f"({num * num1} ÷ {num1})"


# Функция "make_problem_harder" выбирает рандомное число из примера
# и заменяет его выводом одной из четырёх функций: amount, difference, multiplication, division
# пример работы:
# Ввод: "4 + 3"
# Вывод: 4 + 21 ÷ 7
def make_problem_harder(problem, diff=False, mult=False, div=False) -> str:
    functions = [amount]
    if diff:
        functions.append(difference)
    if mult:
        functions.append(multiplication)
    if div:
        functions.append(division)
    range_of_num = random.choice(find_nums(problem))
    new_problem_from_num = random.choice(functions)(int(problem[range_of_num[0]:range_of_num[1]]), problem)
    return f"{problem[:range_of_num[0]]}{new_problem_from_num}{problem[range_of_num[1]:]}"


def problem_gen(level, diff=False, mult=False, div=False):
    new_problem = str(random.randrange(level * 4, level * 5))
    x = new_problem
    for i in range(level * 2):
        new_problem = make_problem_harder(new_problem, diff, mult, div)
    return f"{new_problem}\nответ: {x}"


if __name__ == "__main__":
    level = int(input("Введите уровень сложности примера: "))
    print("Введите операции которые хотите включить (0 или 1 соответственно) в пример в порядке:")
    print("<разность><умножение><деление>(\"010\") без пробелов:")
    operations = [bool(int(i)) for i in list(input())]
    print(problem_gen(level, operations[0], operations[1], operations[2]))
