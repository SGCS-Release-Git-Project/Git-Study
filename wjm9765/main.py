def solve(inputs):
    answers = []
    
    for input in inputs:
        a, b = map(int, input.split())
        answers.append(a * b)
        
    return answers


