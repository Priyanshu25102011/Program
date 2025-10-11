class Computer:
    def __init__(self):
        self.__maxprice = 900   # private variable

    # Getter method
    @property
    def maxprice(self):
        return self.__maxprice

    # Setter method
    @maxprice.setter
    def maxprice(self, price):
        self.__maxprice = price

    # Display method
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))


# Create object
c = Computer()

# Show initial price
c.sell()             # Selling price: 900

# Try changing directly
c.__maxprice = 1000  # This won't affect the private variable
c.sell()             # Still 900

# Use property setter (correct way)
c.maxprice = 1000
c.sell()             # Selling price: 1000

# You can also read it directly
print("Current max price:", c.maxprice)
