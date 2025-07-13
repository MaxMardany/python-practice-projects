def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    for problem in problems:

        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."

        for i in range(len(problem)):
            if problem[i] == '+' or problem[i] == '-':
                operator_index = i
                break

        operator = problem[operator_index]
        left_operand = problem[:operator_index].strip()
        right_operand = problem[operator_index + 1:].strip()

        if not left_operand.isdigit() or not right_operand.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left_operand) > 4 or len(right_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(left_operand), len(right_operand)) + 2

        top = ' ' * (width - len(left_operand)) + left_operand

        bottom = operator + ' ' * (width - len(right_operand) - 1) + right_operand

        dashes = '-' * width

        if show_answers:
            if operator == '+':
                result = str(int(left_operand) + int(right_operand))
            else:
                result = str(int(left_operand) - int(right_operand))
            answer = ' ' * (width - len(result)) + result
            answer_line.append(answer)

        top_line.append(top)
        bottom_line.append(bottom)
        dash_line.append(dashes)

    arranged = '    '.join(top_line) + '\n' + \
               '    '.join(bottom_line) + '\n' + \
               '    '.join(dash_line)

    if show_answers:
        arranged += '\n' + '    '.join(answer_line)

    return arranged

    return problems



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')