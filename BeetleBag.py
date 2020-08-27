# score : 100/100

t = int(input())
for i in range(t):
    val = []
    wt = []
    c, g = input().split()
    c = int(c)
    g = int(g)

    for j in range(g):
        wt_value, pow_value = input().split()
        wt_value = int(wt_value)
        pow_value = int(pow_value)
        wt.append(wt_value) 
        val.append(pow_value) 
  
    K = [[0 for x in range(c + 1)] for x in range(g + 1)]

    for i in range(g + 1):
      for w in range(c + 1):
         if i == 0 or w == 0: 
            K[i][w] = 0
         elif wt[i-1] <= w:
            K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
         else:
            K[i][w] = K[i-1][w]
   
    print(K[g][c])