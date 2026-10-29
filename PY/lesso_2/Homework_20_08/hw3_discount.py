price = float(input("Enter the purchase amount: "))
promo_code = input("Enter promo code: ")

if price >= 5000:
    discount = 15
elif price >= 2000:
    discount = 7
elif promo_code == "QA2026":
    discount = 5
else:
    discount = 0

final_price = price * ( discount / 100)

print(f"Discount: {discount}%")
print(f"Final purchase: {final_price:.2f}")