def solve(inputs):
    answers = []
    #기능
    for input in inputs:
        ans = 0
        for i in range(1, int(input)+1):
            ans += i
        answers.append(str(ans))
        
    return answers