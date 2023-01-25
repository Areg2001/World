from user import User
from product import Product

if __name__ == "__main__":
    user = User("Samo", 121, "sam2000@mail.ru")
    user2 = User("Mxo", 122, "mxo@gmail.com")
    product1 = Product("Phone", 15000, "Iphone, sev, 64Gb")
    product2 = Product("Dress", 1500, "Txamardu, Jins, kapuyt")

    user.add_product(product1)
    user.get_cart()

    user.buy_product(product1)
    user.get_cart()
    user.get_money()

    user.add_product(product2)
    user.get_cart()
    user.get_money()

    user.add_money(12000)
    user.get_money()
    user.remove_product(product2)

    user.get_id()
    user.get_email()
    user.get_name()

    user2.add_product(product2)
    user2.get_cart()

    user2.buy_product(product2)
    user2.get_cart()
    user2.get_money()

    print(user)
    print(user2)

    product1.get_name()
    product1.get_price()

    print(product1)
    print(product2)