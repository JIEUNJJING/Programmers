def solution(s):
    answer = 0
    sum = 0
    s = s.split()

    for i in range(len(s)):
        if s[i] == 'Z':
            sum -= int(s[i - 1])
        else:
            sum += int(s[i])
    answer = sum
    return answer