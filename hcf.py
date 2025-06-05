largenum=int(input("enter largest number:"))
smallnum=int(input("enter your smallest number:"))

while (smallnum):
    numstore=smallnum
    smallnum=largenum%smallnum
    largenumm=numstore

print("HCF/GCD is:",largenum)