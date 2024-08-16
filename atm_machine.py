def atm_machine(amount):
    # Bill values in decreasing order to give the minimum number of bills necessary
    bills = [50, 20, 10, 5, 2]
    bill_count = {}  # Storing the count of each bill
    for i in bills:
        bill_count[i] = amount // i  # Calculate how many of this bill is needed
        amount %= i  # Update the amount with the remainder
    return bill_count

while True:
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount > 200 or amount <= 0:
        print("Invalid amount. Please enter an amount between 1 and 200 Units.")
    else:
        result = atm_machine(amount)
        print("Bills should be given:")
        for bill, count in result.items():
            print("{} Units: {}".format(bill, count))
        break