def crane_position(M):
    # Defining the movement cycle (left -, right +)
    move = [1, -3, -2, 1, 4]
    move_length = len(move)  # Calculating the length of the move list
    
    # Calculating completed cycles and the sum of completed cycles
    completed_cycles = M // move_length
    position_after_completed_cycles = sum(move) * completed_cycles
    
    # Remaining movements after the last complete cycle
    remaining_movements = M % move_length
    position_after_remaining_moves = sum(move[:remaining_movements])
    
    # Addition of the final position values
    P = position_after_completed_cycles + position_after_remaining_moves
    
    # Ensure the position stays within -100 and 100
    if P > 100:
        P = 100
    elif P < -100:
        P = -100
    
    return P

# Taking the input with validation
while True:
    try:
        M = int(input("Enter the minutes passed since starting the crane: "))
        if M > 0:
            position = crane_position(M)
            print("The location of the crane after {} minutes is: {}".format(M, position))
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")