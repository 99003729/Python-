N = int(input())
c = 0
lst=[]
while N>c:
    input_term = input("enter ur command: ").strip().split(" ")
    if input_term[0] == "append":
        lst.append(int(input_term[1]))
        c+=1
    elif input_term[0] == "insert":
        lst.insert(int(input_term[1]), int(input_term[2]))
        c+=1
    elif input_term[0] == "remove":
        lst.remove(int(input_term[1]))
        c+=1
    elif input_term[0] == "pop":
        lst.pop()
        c+=1
    elif input_term[0] == "sort":
        lst.sort()
        c+=1
    elif input_term[0] == "reverse":
        lst.reverse()
        c+=1
    elif input_term[0] == "print":
        print(lst)
        c+=1
