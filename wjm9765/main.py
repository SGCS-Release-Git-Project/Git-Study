def solve(inputs):
    T = int(inputs[0])
    answers = []

    for i in range(1, T + 1):
        a, b = map(int, inputs[i].split())
        answers.append(a + b)

    return answers
