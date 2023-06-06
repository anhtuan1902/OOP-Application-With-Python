class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Create a flatmate person who live in the flat and pay a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pay(self, bill, flatmate2):
        return round((self.days_in_house / (self.days_in_house + flatmate2.days_in_house)) * bill.amount, 2)
