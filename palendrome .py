num=int(input("enter your number:  "))

org_num=num
rev_num=0

while num > 0:
    digit=num%10
    rev_num= rev_num*10+digit
    num//=10
if org_num==rev_num:
    print(org_num,"is a palendrome")

else:
    print(org_num,"is not a palendrome")