def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    layer1 = []
    layer2 = []
    layer3 = []
    layer4 = []

    for problem in problems:
        first, operator, second = problem.split()
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.' 
        width = max(len(first), len(second)) + 2

        layer1.append(first.rjust(width))
        layer2.append(operator + second.rjust(width - 1))
        layer3.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            layer4.append(result.rjust(width))
    arranged = '    '.join(layer1) + '\n'
    arranged += '    '.join(layer2) + '\n'
    arranged += '    '.join(layer3)

    if show_answers:
        arranged += '\n' + '    '.join(layer4)

    return arranged
