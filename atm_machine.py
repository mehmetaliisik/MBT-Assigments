def atm_machine(amount):
    # Initialize the number of each bill to 0
    bill50 = 0
    bill20 = 0
    bill10 = 0
    bill5 = 0
    bill2 = 0
    total = 0  # Initialize total to 0
    
    # Try different combinations of bills range selected according to max withdraw 200 unit
    for bill50 in range(5, -1, -1):  # Check from 5 bills of 50 to 0
        for bill20 in range(11, -1, -1):
            for bill10 in range(21, -1, -1):
                for bill5 in range(41, -1, -1):
                    for bill2 in range(101, -1, -1):
                        # Calculate the total amount for the current combination of bills
                        total = 50 * bill50 + 20 * bill20 + 10 * bill10 + 5 * bill5 + 2 * bill2
                        
                        # If the total matches the amount requested, return the combination of bills
                        if total == amount:
                            bill_count = {50: bill50, 20: bill20, 10: bill10, 5: bill5, 2: bill2}
                            return bill_count

while True:
    try:
        amount = int(input("Enter the amount you want to withdraw: "))
        
        # Check if the entered amount is within the valid range
        if amount > 200 or amount <= 1:
            print("Invalid amount. Please enter an amount between 2 and 200 Units.")
        else:
            # Get the combination of bills needed to dispense the requested amount
            result = atm_machine(amount)
            # Print the breakdown of bills to the user
            print("Bills should be given:")
            for bill, count in result.items():
                if count > 0:
                    print("{} of {} Units".format(count, bill))  # Print the number of each bill type
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a positive integer.")