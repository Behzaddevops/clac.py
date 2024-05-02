print(" _     ___  _   ____  ____  _     ____  _     _     ____  _____  ____  ____ ")
print("/ \__/|\  \//  /   _\/  _ \/ \   /   _\/ \ /\/ \   /  _ \/__ __\/  _ \/  __\.")
print("| |\/|| \  /   |  /  | / \|| |   |  /  | | ||| |   | / \|  / \  | / \||  \/|")
print("| |  || / /    |  \_ | |-||| |_/\|  \_ | \_/|| |_/\| |-||  | |  | \_/||    /")
print("\_/  \|/_/     \____/\_/ \|\____/\____/\____/\____/\_/ \|  \_/  \____/\_/\_\.")

while True :
    print("Please enter the operator + - * / :")
    o=input()
    if o != '+' and o != '-' and o != '*' and o != '/':
        print("Please select the correct operator")
        continue
    else : 
        if o=='+':
            print ("Please enter first number:")
            a=input()
            if a.isnumeric() == False :
                print("Not a number")
                continue
            print ("Please enter second number:") 
            b=input()
            if b.isnumeric() == False :
                print("Not a number")
                continue
            print ("The result is = ",int(a)+int(b))

        if o=='-':
            print ("Please enter first number:")
            a=input()
            if a.isnumeric() == False :
                print("Not a number")
                continue
            print ("Please enter second number:") 
            b=input()
            if b.isnumeric() == False :
                print("Not a number")
                continue
            print ("The result is = ", int(a)-int(b))

        if o=='*':
            print ("Please enter first number:")
            a=input()
            if a.isnumeric() == False :
                print("Not a number")
                continue
            print ("Please enter second number:") 
            b=input()
            if b.isnumeric() == False :
                print("Not a number")
                continue
            print ("The result is = ", int(a)*int(b))
        if o=='/':
            print ("Please enter first number:")
            a=input()
            if a.isnumeric() == False :
                print("Not a number")
                continue
            if a == '0' :
                print ("First value in / not be 0")
                continue
            print ("Please enter second number:") 
            b=input()
            if b.isnumeric() == False :
                print("Not a number")
                continue
            if b == '0' :
                print ("Second value in / not be 0")
                continue
            print ("The result is = ",int(a)/int(b))
        print ("Do you want to continue : any key for yes or n for No ")
        c=input()
        if c=="n":
                break
