def solve(inputs):
    answers = []

    for input in inputs:
        answers.append(sum(list(map(int, input.split()))))

    return answers