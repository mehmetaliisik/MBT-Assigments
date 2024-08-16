This repository contains two Python scripts: crane_position.py and atm_machine.py. These scripts perform specific calculations based on user input and demonstrate basic Python programming concepts such as loops, conditionals, and list operations.

# Factory Crane

The crane_position.py script calculates the position of a crane after a specified number of minutes, based on a predefined movement cycle. The crane moves left and right in a sequence, and the script calculates the crane's final position after a given number of minutes.

### Movement Cycle
The crane follows a specific movement cycle:
- Right by 1 unit
- Left by 3 units
- Left by 2 units
- Right by 1 unit
- Right by 4 units
This sequence repeats as time progresses.

### Script Logic
- Input: The number of minutes passed since the crane started moving.
- Calculation:
    1. The script calculates the number of completed cycles and the sum of movements within these cycles.
    2. It then computes the remaining movements after the last completed cycle.
    3. Finally, the script adds up the position from completed cycles and remaining movements to determine the crane's final position.
- Output: The crane's position after M minutes.

# ATM Machine

The atm_machine.py script simulates an ATM that dispenses bills in denominations of 50, 20, 10, 5, and 2 units. The goal is to dispense the minimum number of bills necessary to fulfill the requested amount.

### Script Logic
- Input: The amount of money to withdraw.
- Validation: The amount must be between 1 and 200 units.
- Calculation:
    1. The script iterates over each bill denomination and determines how many of each bill are needed to make up the requested amount.
    2. The script updates the remaining amount after each denomination is processed.
    Output: The number of each bill denomination to be dispensed.

## Examples

### Factory Crane

- *Input:* Enter the minutes passed since starting the crane: 7
- *Output:* The location of the crane after 7 minutes is: 3

### ATM Machine

- *Input:* Enter the amount you want to withdraw: 127
- *Output:*
Bills should be given:
    - 50 Units: 2
    - 20 Units: 1
    - 10 Units: 0
    - 5 Units: 1
    - 2 Units: 1

## Usage

- Clone the repository to your local machine: 
git clone https://github.com/mehmetaliisik/MBT-Assigments.git

- Run each script individually using Python:
    1. For the Factory Crane:
        python crane_position.py
    2. For the ATM Machine:
        python atm_machine.py