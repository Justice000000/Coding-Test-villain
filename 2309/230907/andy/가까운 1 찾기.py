# https://school.programmers.co.kr/learn/courses/30/lessons/181898

def solution(arr, idx):

    if idx >= len(arr):
        return -1

    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i

    return -1
