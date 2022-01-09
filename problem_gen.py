import random


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


def amount(num, problem) -> str:
    if num > 1:
        num1 = random.randrange(1, num)
        num2 = num - num1
        return f"({num1} + {num2})"
    return num


def difference(num, problem) -> str:
    num1 = random.randrange(num + 1, num * 3)
    num2 = num1 - num
    return f"({num1} - {num2})"


def multiplication(num, problem) -> str:
    divisors = [(int(num / i), i) for i in range(2, num) if num % i == 0]
    if divisors:
        terms = random.choice(divisors)
        if "÷" not in problem and "×" not in problem:  # если в строке нет умножения или деления скобки не нужны
            return f"{terms[0]} × {terms[1]}"
        return f"({terms[0]} × {terms[1]})"
    return num


def division(num, problem) -> str:
    num1 = random.randrange(2, 11)
    if "÷" not in problem and "×" not in problem:  # если в строке нет умножения или деления скобки не нужны
        return f"{num * num1} ÷ {num1}"
    return f"({num * num1} ÷ {num1})"


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
    return f"{new_problem}\nanswer: {x}"


if __name__ == "__main__":
    level = int(input("Problem difficulty level: "))
    print("Enter the operation you want to include (0 or 1, respectively) in problem in order:")
    print("<difference><multiplication><division> for example - '010'")
    operations = [bool(int(i)) for i in list(input())]
    print(problem_gen(level, operations[0], operations[1], operations[2]))
