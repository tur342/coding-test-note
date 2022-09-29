#A - AtCoder社の給料

x = int(input())
y = 0
for num in range(x):
    y+=10000*(num+1)*(1/x)
print(y)