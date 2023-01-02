import qrcode
import pyfiglet
from Film import Film
from Series import Series
from Documentary import Documentary
from Clip import Clip
from Actor import Actor

Actor = []
PRODUCTS = []

def Advanced_search():
    ...

def read_data():
    f = open("Assignment 12/tamrin/data.txt","r")

    for line in f:
        result = line.split(",")
        my_dict = {"code": result[0],"name": result[1],"director": result[2], "IMDB score": result[3], "url": result[4], "duration": result[5], "casts": result[6]}

        PRODUCTS.append(my_dict)
    
    f.close()

def show_menu():
    print("1 = Add")
    print("2 = Edit")
    print("3 = Remove")
    print("4 = Serch")
    print("5 = Show")
    print("6 = Advanced_search")
    print("7 = QR_code")
    print("8 = Exit")
    
def Add():
    code = input("enter code: ")
    name = input("enter name: ")
    director = input("enter director: ")
    IMDBscore = input("enter IMDB score: ")
    url = input("enter url: ")
    duration = input("enter duration: ")
    casts = input("enter casts: ")

    new_product = {"code": code,"name":name,"director":director,"IMDB score":IMDBscore,"url":url,"duration":duration,"casts":casts8}
    PRODUCTS.append(new_product)

def Edit():
    code = input("enter code: ")
    print("name")
    print("price")
    print("count")
    user_input = input()
    new_product = input("input new product: ")

    for product in PRODUCTS:
        if product["code"] == code:
            product[user_input] = new_product
            print("Information updated successfully!!")
            break
    else:
        print("not found")
    print(product)

def Remove():
    a = 0
    code = input("enter code: ")
    for product in PRODUCTS:
        a = a + 1
        if product["code"] == code:
            del PRODUCTS[a-1]
            print("Information Delete successfully!!")
            break
    else:
        print("not found")
    
def QR_code():
    code = input("enter code: ")
    for product in PRODUCTS:
        if product["code"] == code:
            img = qrcode.make(product)
            img.save("product_QR_code.png")
            break
    else:
        print("not found")


def Serch():
    user_input = input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"],"\t\t",product["name"],"\t\t",product["price"],"\t\t")
            break
    else:
        print("not found")
    
def Show_list():
    print("code\t\t\tname\t\t\tdirector\t\tIMDB score\t\t\turl\t\t\t\tduration\t\t\tcasts\t\t\t")
    for product in PRODUCTS:
        print(product["code"],"\t\t",product["name"],"\t\t",product["director"],"\t\t",product["IMDB score"],"\t\t",product["url"],"\t\t",product["duration"],"\t\t",product["casts"],"\t\t")
def write_to_date():
    p = open("Assignment 12/tamrin/data.txt","w")

    for product in PRODUCTS:
        m = product["code"]
        o = product["name"]
        l = product["director"]
        k = product["IMDB score"]
        u = product["url"]
        g = product["duration"]
        j = product["casts"]
        e = m,o,l,k,u,g,j

        p.write(f"{e}\n")

    p.close()
def Buy():
    s = []
    p = []
    while True:
        print("1 = stay, 2 = exit")
        user_input = int(input())
        if user_input == 1:
            user_input = input("code: ")
            for product in PRODUCTS:
                if product["code"] == user_input:
                    count = int(input("enter count: "))
                    if int(product["count"]) >= count:
                        s.append(count)
                        b = int(product["price"])*count
                        p.append(b)
                        product["count"] = int(product["count"]) - count
                        o = product["name"]
                        l = product["price"]
                        k = count
                        m = o,l,k,b
                        Cart.append(m)
                        break
                    else:
                        print("Insufficient inventory")
            else:
                print("not found")
        if user_input == 2:
            for product in Cart:
                print(product)
            print("sum count = ",sum(s))
            print("sum price = ",sum(p))
            break

title = pyfiglet.figlet_format("welcome to my store", font="slant")
print(title)
print("loding...")
read_data()
print("Date loaded.")


while True:

    show_menu()

    choice = int(input("enter your choice: "))

    if choice == 1:
        Add()
    elif choice == 2:
        Edit()
    elif choice == 3:
        Remove()
    elif choice == 4:
        Serch()
    elif choice == 5:
        Show_list()
    elif Advanced_search == 6:
        Buy()
    elif choice == 7:
        QR_code()
    elif choice == 8:
        write_to_date()
        exit(0)
    else:
        print("dorost vared kon")