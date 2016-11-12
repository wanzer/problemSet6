import cs50

print("How much change is owed?")
change=cs50.get_float()*100
while (change<0):
   change=cs50.get_float()*100
coin_25=25
coin_10=10
coin_5=5
coin_1=1
count=0
while (coin_25<=change):
    count+=1
    change-=coin_25
while (coin_10<=change):
    count+=1
    change-=coin_10
while (coin_5<=change):
    count+=1
    change-=coin_5
while (coin_1<=change):
    count+=1
    change-=coin_1
print(count)    




