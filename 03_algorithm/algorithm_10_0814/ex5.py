def powerset(arr, now, result):
    if sum(result) > 10:
        return

    if now == len(arr):
        if sum(result) == 10:
            print(result)
        return
    powerset(arr, now+1, result + [arr[now]])
    powerset(arr, now+1, result)
arr = list(range(1, 11))
powerset(arr, 0, [])