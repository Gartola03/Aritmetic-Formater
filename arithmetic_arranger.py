def arithmetic_arranger(problems, *args):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = []

  for index, value in enumerate(problems):
    operation = value.split(" ")
    if (operation[1] not in "+-"):
      return "Error: Operator must be '+' or '-'."

    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    try:
      value_1 = int(operation[0])
      value_2 = int(operation[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    longest_value = max(len(operation[0]), len(operation[2]))
    width = longest_value + 2

    L1 = f"{operation[0]:>{width}}"
    L2 = operation[1] + f"{operation[2]:>{width-1}}"
    d = '-' * width    

    try:
      arranged_problems[0] += "    " + L1
    except IndexError:
      arranged_problems.append(L1)

    try:
      arranged_problems[1] += "    " + L2
    except IndexError:
      arranged_problems.append(L2)

    try:
      arranged_problems[2] += '    ' + d
    except IndexError:
      arranged_problems.append(d)

    if args:
      try:
        ans = int(operation[0]) + int(operation[2])
        if operation[1] == '-':
          ans = int(operation[0]) - int(operation[2])
        a = f"{ans:>{width}}"
        arranged_problems[3] += "    " + a
      except IndexError:
        arranged_problems.append(a)

  output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
  if args:
    output = output + f"\n{arranged_problems[3]}"
  output = "\n".join(arranged_problems)
  return output