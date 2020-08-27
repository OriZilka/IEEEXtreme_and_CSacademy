# score: 25/100

import numpy as np

t = int(input())

for i in range(t):
    num,name = input().split()
    num = int(num)
    halfLength = int(((len(name) + 1) / 2))
    mis_matchs = 0
    for i in range(halfLength):
        if name[i] != name[len(name)-i-1]:
            mis_matchs += 1
    temp_arr = [num, halfLength, mis_matchs]
    array_size = max(temp_arr)
    res = np.zeros((array_size, array_size, array_size))
    res = np.zeros((500, 500, 500))

    res[0][0][0] = 1
    # print(res)
    for char_changed in range(0, num+1):
        for j in range(1, halfLength+1):
            for mist_num in range(0,mis_matchs+1):
                if(j != len(name)-j+1):
                    if name[j-1] == name[len(name)-j]:
                        res[char_changed][j][mist_num] = res[char_changed][j-1][mist_num] 
                        if(char_changed>=2):
                            res[char_changed][j][mist_num] = (res[char_changed][j][mist_num] + 25 * res[char_changed-2][j-1][mist_num])
                    else:
                        if(mist_num>=1 and char_changed>=1):
                            res[char_changed][j][mist_num] = res[char_changed-1][j-1][mist_num-1] * 2
                        if(char_changed>=2):
                            res[char_changed][j][mist_num] = (res[char_changed][j][mist_num] + 24 * res[char_changed-2][j-1][mist_num-1])  
                else:
                    res[char_changed][j][mist_num] = res[char_changed][j-1][mist_num] 
                    if char_changed>=1:
                        res[char_changed][j][mist_num] = (res[char_changed][j][mist_num] + 25 * res[char_changed-1][j-1][mist_num])
    
    
    # for char_changed in range(0, num+1):
    #         for j in range(1, halfLength+1):
    #             for mist_num in range(0,mis_matchs+1):
    #                 res[char_changed][j][mist_num] = res[char_changed][j][mist_num] % (10**9 + 7)
    
    print(int(res[num][halfLength][mis_matchs] % (10**9 + 7)))
        
