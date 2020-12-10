import sys

num = int(float(input("enter a number: ")))
while num != 0:
    n1= num // 200
    if n1 !=0:
     num = num % 200
     print(f"{n1} 200s")
    
    n2 = num // 100
    if n2 !=0:
         num = num % 100
         print (f"{n2} 100s")

    n3 = num // 50
    if n3 !=0:
        num = num % 50
        print (f"{n3} 50s")

    n4 = num // 20
    if n4 !=0:
        num = num % 20
        print (f"{n4} 20s")

    n5 = num // 10
    if n5 !=0:
        num = num % 10
        print (f"{n5} 10s")
    
    n6 = num // 5
    if n6 !=0:
        num = num % 5
        print (f"{n6} 5s")

    n7 = num // 1
    if n7 !=0:
        num = num % 1
        print (f"{n7} 1s")

        sys.exit(0)