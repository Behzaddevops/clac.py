print(" _     ___  _   ____  ____  _     ____  _     _     ____  _____  ____  ____ ")
print("/ \__/|\  \//  /   _\/  _ \/ \   /   _\/ \ /\/ \   /  _ \/__ __\/  _ \/  __\.")
print("| |\/|| \  /   |  /  | / \|| |   |  /  | | ||| |   | / \|  / \  | / \||  \/|")
print("| |  || / /    |  \_ | |-||| |_/\|  \_ | \_/|| |_/\| |-||  | |  | \_/||    /")
print("\_/  \|/_/     \____/\_/ \|\____/\____/\____/\____/\_/ \|  \_/  \____/\_/\_\.")


while True :
    print("Please enter the function + - * / :")
    a=input()
    if a=='+':
        print ("Please enter first number:")
        a=int(input())
        print ("Please enter second number:") 
        b=int(input())
        print ("the result is = ", a+b)

    if a=='-':
        print ("Please enter first number:")
        a=int(input())
        print ("Please enter second number:")
        b=int(input())
        print ("the result is = ", a-b)

    if a=='*':
        print ("Please enter first number:")
        a=int(input())
        print ("Please enter second number:") 
        b=int(input())
        print ("the result is = ", a*b)

    if a=='/':
        print ("Please enter first number:")
        a=int(input())
        print ("Please enter second number:") 
        b=int(input())
        if  b==0 :
            print("the value is not correct")
            continue
            print ("the result is = ", a/b)
    print ("Do you want to continue : y/n ")
    c=input()
    if c=="n":
            break
