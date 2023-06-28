A= int(input("Nhập A :"))
B= int(input("Nhập B :"))
C= int(input("Nhập C :"))
if A>B:
    if A>C:
        print("A max")
    else:
        if C>B:
            print("C max")
else:
    if B>C:
        print("B max")
    else:
        if C>A:
            print("C max")