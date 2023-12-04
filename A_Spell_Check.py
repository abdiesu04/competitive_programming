in_t_case = int(input())
for i in range(in_t_case):
    n = int(input())
    name = input('')
    s = "Timur"

    lst = [name[i] for i in range(0,len(name))]
    lst.sort()
    lst1 = [s[i] for i in range(0,len(s))]
    lst1.sort()

    if lst == lst1:
        print("Yes")
    else:
        print("No")