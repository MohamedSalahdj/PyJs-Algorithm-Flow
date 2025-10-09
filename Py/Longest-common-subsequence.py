text_01 = "HELLOWORLD"
text_02 = "OHELOD"

n = len(text_01)
m = len(text_02)

dp = [[0] * (n+1) for _ in range(m+1)]


text_01 = " " + text_01
text_02 = " " + text_02


for i in range(1, m+1):
    for j in range(1, n+1):
        if text_02[i] == text_01[j]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print("Length of LCS:", dp[m][n])

# start from the bottom right
# if current value > left value
# -- if current value == top value
# -- -- //the current value inherted from top
#  -- -- move to top row
#  -- else 
#  -- -- // current value is origin of match
#  -- -- add the char to the solution
#  -- -- move to the top row
#  -- -- move to left column
#  move to left column


lcs = ""

i, j = m, n

while i > 0 and j > 0:
    if dp[i][j] > dp[i][j-1]:
        if dp[i][j] == dp[i-1][j]:
            i -=1
        else:
            lcs = text_02[i] + lcs
            i -=1
            j -=1
    else:
        j -=1
    

print("LCS:", lcs)