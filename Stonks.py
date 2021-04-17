import requests

response = requests.get("http://api.altcointrader.co.za/v3/live-stats").json()

DOGE = 791.98308855

x = response['DOGE']
DValue = float(x["Price"]) * DOGE
print("Current Price: " +x["Price"])
print("Current Volume: " +x["Volume"])
print("Current High: " +x["High"])
print("Current Low: " +x["Low"])
print("Current Selling Price: " +x["Sell"])
print("Current Buying Price: " +x["Buy"])

print("Current Doge Value : " + str(DValue))
