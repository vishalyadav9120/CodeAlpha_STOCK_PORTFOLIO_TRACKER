# CodeAlpha Internship
# Task 2 - Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

print("=" * 45)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 45)

total_investment = 0
portfolio = {}

while True:
    stock_name = input("\nEnter Stock Name (AAPL/TSLA/GOOGL/MSFT/AMZN): ").upper()

    if stock_name not in stock_prices:
        print("❌ Stock not available. Try again.")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    more = input("Do you want to add another stock? (yes/no): ").lower()

    if more != "yes":
        break

print("\n" + "=" * 45)
print("PORTFOLIO SUMMARY")
print("=" * 45)

result = ""

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    line = f"{stock} -> {quantity} Shares × ${price} = ${investment}"
    print(line)
    result += line + "\n"

print("-" * 45)
print(f"Total Investment = ${total_investment}")

result += "-" * 45 + "\n"
result += f"Total Investment = ${total_investment}"

# Save result to text file
with open("portfolio_summary.txt", "w") as file:
    file.write(result)

print("\n✅ Portfolio saved successfully in 'portfolio_summary.txt'")