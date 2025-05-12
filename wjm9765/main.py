def solve(inputs):
    # 첫 번째 문자열을 줄 단위로 나눈다
    lines = inputs[0].splitlines()
    
    T = int(lines[0])
    answers = []
    
    for i in range(1, T + 1):
        a, b = map(int, lines[i].split())
        answers.append(a + b)
    
    return answers
