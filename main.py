from aims.dvd import DigitalVideoDisc
from aims.cart import Cart


def main():
    # Create some DVDs
    dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
    dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 124, 24.95)
    dvd3 = DigitalVideoDisc("Aladdin", "Animation", "Ron Clements", 90, 18.99)

    # Create a cart and add DVDs
    cart = Cart()
    cart.add_dvd(dvd1)
    cart.add_dvd(dvd2)
    cart.add_dvd(dvd3)

    # Display total cost
    print(f"Total cost: {cart.total_cost()} $")


if __name__ == "__main__":
    main()
