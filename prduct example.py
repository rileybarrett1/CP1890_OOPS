from classes import product


def main():

    while True:
        print("\nThe Product Viewer program")
        print("1.Stanley 13 ounce wood hammer")
        print("2.National Hardware 3/4 Wire nails")
        print("3.economy duct tape,60 yds silver, silver")
        user_input = input("enter product number:")

        # creating products
        product1 = product("Stanley 13 ounce wood hammer", 12.99, 5)
        product2 = product("National Hardware 3/4 Wire nails", 2.00, 4)
        product3 = product("economy duct tape,60 yds silver, silver", 9.99, 6)

        if user_input == "1":
            print("\nProduct data")
            print(f"Product Name:\t\t{product1.name}")
            print(f"Product Price:\t\t{product1.price}")
            print(f"Discount Percent:\t{product1.discountpercent:d}%")
            print(f"Discount Amount:\t{product1.getDiscountamount():.2f}")
            print(f"Discount Price:\t\t{product1.getdiscountprice():.2f}")
        if user_input == "2":
            print("\nProduct data")
            print(f"Product Name:\t\t{product2.name}")
            print(f"Product Price:\t\t{product2.price}")
            print(f"Discount Percent:\t{product2.discountpercent:d}%")

            print(f"Discount Amount:\t{product2.getDiscountamount():.2f}")
            print(f"Discount Price:\t\t{product2.getdiscountprice():.2f}")
        if user_input == "3":
            print("\nProduct data")
            print(f"Product Name:\t\t{product3.name}")
            print(f"Product Price:\t\t{product3.price}")
            print(f"Discount Percent:\t{product3.discountpercent:d}%")

            print(f"Discount Amount:\t{product3.getDiscountamount():.2f}")
            print(f"Discount Price:\t\t{product3.getdiscountprice():.2f}")
        try:
            if user_input < '1' or user_input > '3':
                print("invalid number please select a number from 1 to 3")
        except ValueError:
            print("invalid number, please try again")

        cont = input("Do you want to continue y/n: ").lower()
        if cont == "y":
            main()
        else:
            print("Goodbye")
        break


if __name__ == "__main__":
    main()