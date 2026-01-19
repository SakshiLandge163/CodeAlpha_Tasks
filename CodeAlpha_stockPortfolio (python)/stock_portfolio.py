stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL": 140,
    "AMZN" : 130,
}

total_investment = 0

print("Available Stocks:",list(stock_prices.keys()))

while True:
    stock = input("Enter stock name ( or type 'done' to finish):").upper()
    
    if stock =="DONE":
        break
    
    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock]*quantity
        total_investment += investment
        print(f"Added{stock}: Rs{investment}")
    else:
        print("Stock not avalilable!")
        
print("\nTotal Investement Value Rs :", total_investment)

with open("portfolio.txt","w") as file:
    file.write(f"Total Investment Value: Rs{total_investment}")
    
print("Portfolio saved to portfolio.txt")