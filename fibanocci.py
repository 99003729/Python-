num = int(input())

def fibonacci(n):
    count = 0
    no_1=0
    no_2=1
    if n<=0:
        print("Enter a positive integer only!")
    elif n==1:
        print(no_1)
    else:
        while count < n:
            print(no_1)
            output_no = no_1 + no_2
            no_1 = no_2
            no_2 = output_no
            count +=1

fibonacci(num)
