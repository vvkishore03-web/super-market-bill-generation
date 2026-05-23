# Super Market Bill Generation

print("===== SUPER MARKET BILL =====")

items = []
prices = []
quantities = []

total = 0

while True:
    item = input("Enter Item Name: ")
    price = float(input("Enter Item Price: ₹"))
    qty = int(input("Enter Quantity: "))

    items.append(item)
    prices.append(price)
    quantities.append(qty)

    total += price * qty

    more = input("Add more items? (yes/no): ").lower()

    if more != "yes":
        break

discount = 0

if total >= 500:
    discount = total * 0.10

final_total = total - discount

print("\n========== BILL ==========")
print("Item\tPrice\tQty\tTotal")

for i in range(len(items)):
    item_total = prices[i] * quantities[i]
    print(f"{items[i]}\t₹{prices[i]}\t{quantities[i]}\t₹{item_total}")

print("--------------------------")
print("Subtotal: ₹", total)
print("Discount: ₹", discount)
print("Final Amount: ₹", final_total)

print("Thank You! Visit Again")