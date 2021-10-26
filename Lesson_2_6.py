stuff = {"name": [],'price': [], 'quantity':[]}
while True:
    value = input('Введите наименование товара - ')
    if value != "":
        stuff['name'].append(value)
    else:
        break
    value_price = int(input('Введите стоимость товара - '))
    if value_price != '':
        stuff['price'].append(value_price)
    value_quantity = int(input('Введите количество товара - '))
    if value_quantity != '':
        stuff['quantity'].append(value_quantity)
# print(stuff)


products = []
for i in range(len(list(stuff.values())[0])):
    product = {'name':list(stuff.values())[0][i], 'price': list(stuff.values())[1][i],
               'quantity': list(stuff.values())[2][i]}
    products.append(product)
    # print(product)
# print(products)

goods = []
for i in range(len(products)):
    print(products[i])
    goods.append(((i+1), products[i]))
print(goods)