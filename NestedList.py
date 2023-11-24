if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
  
    scores = list(set([x[1] for x in students]))
    scores.sort()
    second_min = scores[1]
    min_name = [x[0] for x in students if x[1] == second_min]
    min_name.sort()
    for i in min_name:
        print(i)


#Nested List Litcode
    
