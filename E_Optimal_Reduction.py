for _ in range(int(input())):
    n = int(input()) 
    a = [int(i) for i in input().split()] 
    ans = "YES" 
    c = False
    for i in range(1, n): 
        if a[i-1] > a[i] : c = True 
        elif a[i-1] < a[i] and c : ans = "NO"; break 
    print(ans)