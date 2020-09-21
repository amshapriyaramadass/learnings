if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    person_names={}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # another way to get marks marks = student_marks(query_name)
    marks = student_marks.get(query_name)
    
    total = 0.00
    for a in marks:
        print(total)
        total += a 
    # another way of writing this output 
    # print("{:.2f}".format(sum(marks)/(len(marks))))

    print("{:.2f}".format(total/len(marks)))


        
     
