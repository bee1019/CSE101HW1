# CSE 101, Fall 2018
# Assignment 1 starter code
#
# Your name: Bansri Shah
# Your SBU ID: 110335850

# Complete the function that follows for this assignment

import string

def alfg(sequence, rounds):
    first_num = 0
    sec_num = 1
    new_seq = []
    
    for j in sequence:
        new_seq.append(j)
    
    for i in range(rounds):
        temp = new_seq[first_num] + new_seq[sec_num]
        new_seq.append(temp%10)
        first_num += 1
        sec_num += 1
    if len(new_seq) >= 5:
        return new_seq[len(new_seq) - 5 : ]
    else:
        return new_seq # CHANGE OR REPLACE THIS STATEMENT


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Problem 1: Lagged Fibonacci Digits
    init_sequence = []
    next_value = 10 # we need a multi-digit value other than -1 to force the loop to begin
    while next_value != -1 and next_value > 9:
        next_value = int(input("Enter the next digit in the initial sequence, or -1 to end: "))
        if next_value != -1 and next_value < 10:
            init_sequence.append(next_value)
            next_value = 10 # force the loop to continue after a single digit is entered
    rds = int(input("Enter the number of rounds to perform: "))

    print("Calling alfg() with the starting sequence", init_sequence, "and", rds, "rounds, for a final result of", alfg(init_sequence,rds))
    print()

