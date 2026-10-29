price= int(input('Enter price: '))
discount= int(input('Enter discount: '))
final_price= price - (price * discount / 100)
print(f'Final price is {final_price} USD')