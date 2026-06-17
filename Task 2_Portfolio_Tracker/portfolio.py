stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 170
}

total = 0

print("=== STOCK PORTFOLIO TRACKER ===")

while True:

    stock = input("\nEnter Stock Name (or type DONE): ").upper()

    if stock == "DONE":
      break

if stock in stock_prices:

        quantity = int(input("Enter Quantity: "))

        value = stock_prices[stock] * quantity

        total += value

        print("Added Value:", value)

else:
        print("Stock not available")
print("\nTotal Investment Value =", total)
