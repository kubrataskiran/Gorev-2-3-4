n = int(input("the number of years of house="))
price = list(map(int,input().split())) #enter price values
di = {price[i]:i for i in range(n)} #add entered prices to list
price = sorted(price)
#m=10000000
m=10^16 #max price
#if the following price lower find min loss value with taking the difference
for i in range(1,n):
    if di[price[i]]<di[price[i-1]]: 
        m=min(m,price[i]-price[i-1]) 
print(m)