e = int(input("english:"))
m = int(input("math:"))
if (e >= 0 and e<=100) and (m >= 0 and m<=100):
    if m >= 90 and e >= 90:
        print("good")
    elif m < 60 and e < 60:
        print("bad")
    elif m < 60 or e < 60:
        print("soso")
else:
    print('!!ERROR!!')
