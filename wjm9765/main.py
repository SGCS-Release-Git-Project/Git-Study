def solve(inputs):
    answers = []
    for input_line in inputs:
        a, b = map(int, input_line.split())
        answers.append(a + b)
    return answers
