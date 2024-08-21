def atm_machine(amount):
    # Bill values in decreasing order to give the minimum number of bills necessary
    bills = [50, 20, 10, 5, 2]
    bill_count = {}  # Storing the count of each bill
    for i in bills:
        bill_count[i] = amount // i  # Calculate how many of this bill is needed
        amount %= i  # Update the amount with the remainder
    return bill_count, amount

while True:
    try:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount > 200 or amount <= 1:
            print("Invalid amount. Please enter an amount between 2 and 200 Units.")
        else:
            result, remainder = atm_machine(amount)
            if remainder == 0:
                print("Bills should be given:")
                for bill, count in result.items():
                    if count > 0:
                        print("{} of {} Units".format(count, bill))
            else:
                print("The machine cannot dispense the exact amount. Please enter a different amount.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")