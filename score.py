s = int(input("your score:"))
if s >= 0 and s<=100:
    if s >= 90:
        print("A")
    elif s >= 80:
        print("B")
    elif s >= 70:
        print("C")
    elif s >= 60:
        print("D")
    else:
        print("E")
else:
    print("錯誤")

