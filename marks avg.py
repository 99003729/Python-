n = int(input("enter the number of students mark u want to enter "))
while 2<=n<=10:
    student_marks = {}
    for _ in range(n):
        name, *line = input("enter name and marks with space").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("enter the student query name ")
    if query_name in student_marks:
        output_ans=sum(student_marks[query_name])/len(student_marks[query_name])
        print(output_ans)
        break
    else: print("error")