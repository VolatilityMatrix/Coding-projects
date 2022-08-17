K = int(input())
L = int(input())
M = int(input())
N = int(input())
counter = 0
hasEnded = False
i = K
while (i <= 8):
    j = 9
    while (j >= L):
        k = M
        while (k <= 8):
            l = 9
            while (l >= N):
                isPossible = i % 2 == 0 and k % 2 == 0 and l % 2 != 0 and j % 2 != 0
                firstNum = i * 10 + j
                secondNum = k * 10 + l
                if (isPossible and firstNum == secondNum):
                    print("Cannot change the same player.")
                elif (isPossible and firstNum != secondNum):
                    print(f"{i}{j} - {k}{l}")
                    counter += 1
                if (counter >= 6):
                    hasEnded = True
                if (hasEnded):
                    break
                l -= 1
            if (hasEnded):
                break
            k += 1
        if (hasEnded):
            break
        j -= 1
    if (hasEnded):
        break
    i += 1