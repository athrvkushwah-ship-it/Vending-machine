from pymongo import MongoClient

Client = MongoClient("mongodb://localhost:27017/")
db = Client["vending_machinn_db"]
collection = db['products']

def admin():
    operate = input('Insert or delete item:')
    if operate == 'Insert':
        code = input("Enter new product code: ").strip().upper()
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter initial stock: "))
        collection.insert_one({"code": code, "name": name, "price": price, "stock":stock },)
    elif operate == 'Delete':
        code = input("Enter new product code: ").strip().upper()
        collection.delete_one({'code':code})

def check():
    password = 'xyz@792'
    print('pls inter password to open admibn menu')
    passw = input('Enter the password')
    if passw ==password:
        print('admin page')
        admin()

def purchase(item,quantity):
    amount = item['price']*quantity
    print(amount)
    bill = float(input('pay the bill : '))
    if bill<amount:
        print('lesser amount')
    elif bill==amount:
        print('dispatched')
        collection.update_one(
            {'code' : item['code']},
            {"$inc":{'stock':-quantity}}
        )
      
product = [
  {"code": "A1", "name": "Coke", "price": 2.50, "stock": 5},
  {"code": "A2", "name": "Pepsi", "price": 2.50, "stock": 4},
  {"code": "B1", "name": "Chips", "price": 1.50, "stock": 6},
  {"code": "B2", "name": "Chocolate", "price": 2.00, "stock": 3},
  {"code": "C1", "name": "Water", "price": 1.00, "stock": 8}
]

# collection.insert_many(product)

for item in collection.find({}):
    print(item)

A = input('Enter product code :')
quantity = int(input('enter the prod qnt :'))
for item in collection.find({"code" : A }):
    if not item:
        print('Not found')
    elif item['stock'] >=quantity:
        print('Choose payment method')
        purchase()
    else:
        print('out of stock')