import requests


response = requests.get("http://api.altcointrader.co.za/v3/live-stats").json()

DOGE = 791.98308855 

print("********************__Doge__********************")
x = response['DOGE']
DValue = float(x["Price"]) * DOGE
print("Current Price: " +x["Price"])
print("Current Volume: " +x["Volume"])
print("Current High: " +x["High"])
print("Current Low: " +x["Low"])
print("Current Selling Price: " +x["Sell"])
print("Current Buying Price: " +x["Buy"])

print("Current Doge Value : " + str(DValue))

print("___________________________________________________")

BTT = 1380.56250000
y = response["BTT"]

print("********************__BTT__********************")

BValue = float(y["Price"]) * BTT
print("Current Price: " +y["Price"])
print("Current Volume: " +y["Volume"])
print("Current High: " +y["High"])
print("Current Low: " +y["Low"])
print("Current Selling Price: " +y["Sell"])
print("Current Buying Price: " +y["Buy"])

print("Current BTT Value : " + str(BValue))
print("___________________________________________________")
print("Total Portfolio Value = R " +  str(BValue+DValue))

PROFIT = ((BValue + DValue)-1200)
print("Total Profit so far = R " + str(PROFIT))


