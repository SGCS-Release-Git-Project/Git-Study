def solve(inputs):
    answers = []
    
    for input in inputs:
        ans = 0
        for i in range(1, int(input)+1):
            ans += i
        answers.append(str(ans))
        
    return answers