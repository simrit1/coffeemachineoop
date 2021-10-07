class Cashier:
    CURRENCY = "DKK"

    COIN_VALUES = {"DKK"}

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Print profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Return total based on coins inserted"""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: "))
        return self.money_received

    def make_payment(self, cost):
        """True if payment is accepted, False if declined."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Proccesing refund.")
            self.money_received = 0
            return False

    def credit_card(self, cost):
        """True if card is inserted"""
        self