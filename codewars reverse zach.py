#zach piening
#reverse reverse
x=input("put in your string")
s=len(x)-1
print(x)
for i in range(0,len(x)):
    print(x[s],end="")
    s=s-1
