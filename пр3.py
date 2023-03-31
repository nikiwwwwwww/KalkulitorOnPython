import mysql.connector
import random 
import re

global mylistproduct
global mylistprice
global summa
global phone
global mylistcount
global role
mylistproduct = []
mylistprice = []
mylistcount = []
summa = 0.00

class Hotdog:
    def __init__(self, sausage, bun, ketchup, mustard, onion, cheese, pickle, jalapeno, koreancarrot):
        self.sausage = sausage #сосиска
        self.bun = bun #булка
        self.ketchup = ketchup #кетчупе
        self.mustard = mustard #горчица
        self.onion = onion #лук
        self.cheese = cheese #сыр
        self.pickle = pickle #огурчик
        self.jalapeno = jalapeno #холопеньо
        self.koreancarrot = koreancarrot #морковь корейская
    
    def __str__(self):
        return f"Hotdog with {self.sausage}, {self.bun}, {self.ketchup}, {self.mustard}, {self.onion}, {self.relish}, and {self.cheese}"

def check_login(username, password):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT Login_polsovatel, Password_polsovatel FROM polsovatel WHERE Login_polsovatel = %s AND Password_polsovatel = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    mydb.close()
    if result:
        return True
    else:
        return False

def getbalance(username):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT balance FROM polsovatel WHERE Login_polsovatel = %s;"
    cursor.execute(query, [username])
    result = cursor.fetchone()
    balance = result[0]
    mydb.close()
    return balance

def new_login(username,password):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    bal = 0.0
    query = "insert into polsovatel (Login_polsovatel, Password_polsovatel,balance,history_count,history_summ) values(%s,%s,%s,%s,%s)"
    values = (username,password, bal,0,0)
    cursor.execute(query,values)
    mydb.commit()

def getproductProduct(id):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT product FROM sklad WHERE ID_sklad = %s;"
    cursor.execute(query, [id])
    result = cursor.fetchone()
    product = result[0]
    mydb.close()
    return product

def getproductPrice(id):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT price FROM sklad WHERE ID_sklad = %s;"
    cursor.execute(query, [id])
    result = cursor.fetchone()
    price = result[0] 
    mydb.close()
    return price

def new_history(prod, summ,id):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    bal = 0.0
    query = "insert into history_polzovatel (product, summa,Polzovatel_ID) values(%s,%s,%s);"
    cursor.execute(query,(prod, summ, id))
    mydb.commit()

def gethistorycount(username):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT history_count FROM polsovatel WHERE Login_polsovatel = %s;"
    cursor.execute(query, [username])
    result = cursor.fetchone()
    history_count = result[0]
    mydb.close()
    history = history_count % 5
    return history

def gethistorycountprosto(username):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT history_count FROM polsovatel WHERE Login_polsovatel = %s;"
    cursor.execute(query, [username])
    result = cursor.fetchone()
    history_count = result[0]
    mydb.close()
    return history_count

def check_phone(phone):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT history_summ FROM polsovatel WHERE phone = %s;"
    cursor.execute(query, [phone])
    result = cursor.fetchone()
    history_summ = result[0]
    mydb.close()
    
    return history_summ

def upd_balance(balance,username):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "update polsovatel set balance = %s where Login_polsovatel = %s;"
    values = (balance,username)
    cursor.execute(query,values)
    mydb.commit()

def getIDPolzovatel(username):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT ID_polsovatel FROM polsovatel WHERE Login_polsovatel = %s;"
    cursor.execute(query, [username])
    result = cursor.fetchone()
    balance = result[0]
    mydb.close()
    return balance

def getollhistory(username,ID):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    id = getIDPolzovatel(username)
    query = "SELECT product, summa FROM history_polzovatel WHERE Polzovatel_ID = %s and ID_history_polzovatel = %s;"
    cursor.execute(query, (id,ID))
    product,summ = cursor.fetchone()
    print(f"product = {product}; summa = {summ}\n")
    mydb.close()
    

def updColvoInSklad(count,ID_skald):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "update sklad set count = %s where ID_sklad = %s;"
    values = (count,ID_skald)
    cursor.execute(query,values)
    mydb.commit()

def getColvoInSklad(ID_skald):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT count FROM sklad WHERE ID_sklad = %s;"
    cursor.execute(query, [ID_skald])
    result = cursor.fetchone()
    count = result[0]
    mydb.close()
    return count
    
def check_phone(phone):
    mydb = mysql.connector.connect(host="localhost", database="Hotdogjnai", user="root", password="1234" )
    cursor = mydb.cursor()
    query = "SELECT Login_polsovatel FROM polsovatel WHERE phone_number = %s"
    cursor.execute(query, phone)
    result = cursor.fetchone()
    mydb.close()
    if result:
        return True
    else:
        return False

        


role = False
#TODO Для входы 
print("Добро пожаловать в Хотдожную 'У дороги'\n")
print("1. Авторизация\n"
      "2. Регистрация\n")
polz = 0
command = input()
match command.split():
    case["1"]:
        q = True
        while(q):
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if check_login(username, password):
                print("Авторизация прошла успешно")
                balance = getbalance(username)
                polz = 1
                if(username == "admin"):
                    role = True 
                else: role = False
                q = False
            else:
                print("Неверные имя пользователя или пароль")
                q = True

    case["2"]:
        username = input("Введите логин")
        password = input("Введите пароль")
        new_login(username,password)
        polz = 0

vixod = False

#TODO Для Пользователя
if(role == False):
    while(vixod == False):
        command = int(input("1.Новый заказ\n2. история\n3.баланс\n4.выход\n"))
        polz = 0

        upd_balance(1000,username)
        print("баланс пополнен")
        #TODO Заказ
        if(command == 1):
            for id in range(1,10):
                productProduct = ""
                productPrice = ""
                count = 0
                productProduct = getproductProduct(id)
                productPrice = getproductPrice(id)
                vibor = input(f"вы хотите добавить {productProduct} по цене {productPrice}\n1 - да\n2 - нет\n")
                if(vibor == "1"):
                    colvo = int(input(f"сколько хотите добавить {productProduct}\n"))
                    productPrice *= colvo
                    mylistproduct.append(productProduct)
                    mylistprice.append(productPrice)
                    mylistcount.append(colvo)
                    count = getColvoInSklad(id)
                    if((count - colvo) <0 ):
                        print("Продукты кончились")
                    else:
                        count = count - colvo
                    updColvoInSklad(count, id)
                    balance = getbalance(username)
                    if((balance - summa - productPrice)<0):
                        print("Недостаточно средств\n")
                    else:
                        summa = summa + productPrice
                    print(summa)
                else:
                    print()
            if(gethistorycount(username) == 0):
                print("Поздравляем вы получили скидку 30%!\n")
                summa -= summa * 30 / 100
                print(summa)
            ranch = random.randint(1,6)
            if(ranch == 5):
                print("У вас утконос\n")
                summa = summa - summa * 30 / 100 
                print("вы получаете скидку 30%")
            else:
                print(f"с едой все хорошо ({ranch}) \n")
            print("А у вас есть карта лояльности?\n")
            phone = input("скажите мне ваш телефон(без пробелов и лишних символов типа 8921234567) если его нет то ничего не пишите: \n")
            if(phone==""):
                print()
            elif(phone.__len__()>11):
                print()
            elif(15000>check_phone(phone) and check_phone(phone)>5000):
                print("Ваша скидка 5%")
                summa = summa - summa * 5 / 100 
            elif(25000>check_phone(phone) and check_phone(phone)>15000):
                print("Ваша скидка 10%")
                summa = summa - summa * 10 / 100 
            elif(check_phone(phone)>25000):
                print("Ваша скидка 20%")
                summa = summa - summa * 20 / 100 
            else:
                print("ну и ладушки)\n")
            if(polz == 0):
                balance = summa + summa * 30 / 100
            print(f"Ваш баланс: {balance}\n")
            print("Производится оплата\n")
            print(summa)
            upd_balance(balance, username)
            baladmin = getbalance("admin")
            baladmin=baladmin+summa
            upd_balance(baladmin, "admin")
            prod = "hotdog"
            id = getIDPolzovatel(username)
            new_history(prod, summa, id)

            # print("Запись в чек")

            # with open("C:\\Users\\nik_s\\Desktop\\Лекции\\3 курс\\Питон\\пр3\\check.txt", 'r') as f: 
            #     text = f.read()
            #     f.close()

            # clean_text = re.sub(r'[^a-zA-Z0-9\n]', ' ', text)

            # lines = clean_text.split('\n')

            # with open('check.txt', 'w') as f:
            #     f.write("Чек\n")
            #     for item in mylistproduct:
            #         f.write(item)
            
            # with open('check.txt', 'w') as f:
            #     f.write("Чек\n")
            #     for item in mylistprice:
            #         f.write(item)
            
            # with open('check.txt', 'w') as f:
            #     f.write("Чек\n")
            #     for item in mylistcount:
            #         f.write(item)

        elif(command == 2):
            i = gethistorycountprosto(username)
            for j in range(1, i):
                getollhistory(username,j)
            

        elif(command == 3):
            balance = getbalance(username)
            print(balance)

        elif(command == 4):
            vixod = True
            break


#TODO Для администратора
elif(role == True):
    while(vixod == False):
        vibor = int(input("Выберите действие:\n 1.узнать баланс\n2.закупки\n3.история покупок пользователя\n4.узнать карту лояльности\n"))
        if(vibor == 1):
            balance = getbalance(username)
            print(balance)
        elif(vibor == 2):
            for id in range(1,10):
                productProduct = ""
                productPrice = ""
                count = 0
                productProduct = getproductProduct(id)
                productPrice = getproductPrice(id)
                productPrice = productPrice - productPrice / 15 * 100
                vibor = input(f"вы хотите купить {productProduct} по цене {productPrice}\n1 - да\n2 - нет\n")
                if(vibor == "1"):
                    colvo = int(input(f"сколько хотите купить {productProduct}\n"))
                    productPrice *= colvo
                    mylistproduct.append(productProduct)
                    mylistprice.append(productPrice)
                    mylistcount.append(colvo)
                    count = getColvoInSklad(id)
                    count = count + colvo
                    updColvoInSklad(count, id)
                    summa = summa + productPrice
                    print(summa)
                else:
                    print()
            balance = getbalance(username)
            balance = balance - summa
            upd_balance(balance, username)

        elif(vibor == 3):
            userhistory = input("Введите логин пользователя\n")
            i = gethistorycountprosto(userhistory)
            for j in range(1, i):
                getollhistory(userhistory,j)

        elif(vibor == 4):
            phone = input("Введите номер телефона\n")
            if(check_phone(phone)):
                print("карта есть\n")
            else: 
                print("Карты нет\n")
        







