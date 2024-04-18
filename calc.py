print(" _     ___  _   ____  ____  _     ____  _     _     ____  _____  ____  ____ ")
print("/ \__/|\  \//  /   _\/  _ \/ \   /   _\/ \ /\/ \   /  _ \/__ __\/  _ \/  __\.")
print("| |\/|| \  /   |  /  | / \|| |   |  /  | | ||| |   | / \|  / \  | / \||  \/|")
print("| |  || / /    |  \_ | |-||| |_/\|  \_ | \_/|| |_/\| |-||  | |  | \_/||    /")
print("\_/  \|/_/     \____/\_/ \|\____/\____/\____/\____/\_/ \|  \_/  \____/\_/\_\.")


while True :
    print("Please enter the funtction + - * / :")
    a=input()
    if a=='+':
        print ("please enter first number:")
        a=int(input())
        print ("please enter secend number:") 
        b=int(input())
        print ("the resulte is = ", a+b)

    if a=='-':
        print ("please enter first number:")
        a=int(input())
        print ("please enter secend number:")
        b=int(input())
        print ("the resulte is = ", a-b)

    if a=='*':
        print ("please enter first number:")
        a=int(input())
        print ("please enter secend number:") 
        b=int(input())
        print ("the resulte is = ", a*b)

    if a=='/':
        print ("please enter first number:")
        a=int(input())
        print ("please enter secend number:") 
        b=int(input())
        if  b==0 :
            print("the value is not corect")
            continue
            print ("the resulte is = ", a/b)
    print ("Do you want to continue : y/n ")
    c=input()
    if c=="n":
            break
