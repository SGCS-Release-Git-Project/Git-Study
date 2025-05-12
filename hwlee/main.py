def solve(inputs):
    answers = []

    for input in inputs:
        n = int(input)
        dp = [-1]*91
        ans = logic(n, dp)
        answers.append(str(ans))

    return answers

def logic(n, dp):
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]