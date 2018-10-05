if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner = max(arr)
    for i in range(n):
        if winner == max(arr):
            list.remove(max(arr))
            i= i+1
    print(max(arr))