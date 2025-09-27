#!/usr/bin/python
from subprocess import *

# 1:UCS+, 2:UCS-, 3:CS1+, 4:CS1-, 5:CS2+, 6:CS2-

# Ask user how many population fly wants to be tested
population = int(raw_input("Population of fruit flies to test: "))
config = raw_input("Configuration file(basic.cfg or basicP.cfg or basicNew.cfg): ") 
    
# Split population half and half
first_half = population // 2
second_half = population - first_half

print("First half (CS1 testing): {} flies".format(first_half))
print("Second half (CS2 testing): {} flies".format(second_half))
print("=" * 60)

# Initialize counters
first_half_responses = 0
second_half_responses = 0

# For each fly 1st half
print("First Half with CS1")
print("=" * 40)

for fly_num in range(first_half):
        
    # Start ca pip Popen
    pid = Popen(["/home/bls96/bin/ca", config], stdin=PIPE, stdout=PIPE)
        
    # First order conditioning
    # print("  - First order conditioning")
    """First order conditioning (CS1 + UCS)"""
    for trials in range(3):
        for pulses in range(12):
            pid.stdin.write("3/1\n")  # CS1+
            x = pid.stdout.readline()

            pid.stdin.write("4/1\n")  # CS1-
            x = pid.stdout.readline()

            pid.stdin.write("0/1\n")
            x = pid.stdout.readline()

            pid.stdin.write("1/1\n")  # UCS+
            x = pid.stdout.readline()

            pid.stdin.write("2/1\n")  # UCS-
            x = pid.stdout.readline()

            pid.stdin.write("0/1\n")  # Rest
            x = pid.stdout.readline()
        
    # Second order conditioning  
    for trials in xrange(3):
        pid.stdin.write("5/1\n")
        x = pid.stdout.readline()

        pid.stdin.write("6/1\n")
        x = pid.stdout.readline()

        pid.stdin.write("0/1\n")
        x = pid.stdout.readline()

        for pulses in xrange(12):
            
            pid.stdin.write("3/1 5/1\n")    #CS1+ & CS2+
            x = pid.stdout.readline()

            pid.stdin.write("4/1 6/1\n")   #CS1- & CS2-
            x = pid.stdout.readline()

        pid.stdin.write("0/1\n")
        x = pid.stdout.readline()
        
    # Test CS1
    pid.stdin.write("3/1\n")  # CS1+
    x = pid.stdout.readline()

    # Count response "1" of learning behavior
    if x[0] == "1":
        first_half_responses += 1
        response_result = 1
    else:
        response_result = 0
        
    pid.stdin.write("4/1\n")  # CS1-
    x = pid.stdout.readline()
        
    pid.stdin.write("0/1\n")  # Rest
    x = pid.stdout.readline()

    print("  - Fly #{}: CS1 response = {}".format(fly_num + 1, response_result))
        
    # Close pid.stdin and read
    pid.stdin.close()
    print

print

# For each fly 2nd half  
print("Second Half with CS2")
print("=" * 40)

for fly_num in xrange(second_half):
        
    # Start ca pip Popen
    pid = Popen(["/home/bls96/bin/ca", config], stdin=PIPE, stdout=PIPE)
        
    # First order conditioning
    for trials in range(3):
        for pulses in range(12):
            pid.stdin.write("3/1\n")  # CS1+
            x = pid.stdout.readline()

            pid.stdin.write("4/1\n")  # CS1-
            x = pid.stdout.readline()

            pid.stdin.write("0/1\n")
            x = pid.stdout.readline()

            pid.stdin.write("1/1\n")  # UCS+
            x = pid.stdout.readline()

            pid.stdin.write("2/1\n")  # UCS-
            x = pid.stdout.readline()

            pid.stdin.write("0/1\n")  # Rest
            x = pid.stdout.readline()
        
    # Second order conditioning  
    for trials in xrange(3):
        pid.stdin.write("5/1\n")    #CS2+
        x = pid.stdout.readline()

        pid.stdin.write("6/1\n")     #CS2-
        x = pid.stdout.readline()

        pid.stdin.write("0/1\n")
        x = pid.stdout.readline()

        for pulses in xrange(12):
            
            pid.stdin.write("3/1 5/1\n")     #CS1+ & CS2+
            x = pid.stdout.readline()

            pid.stdin.write("4/1 6/1\n")     #CS1- & CS2-
            x = pid.stdout.readline()

            pid.stdin.write("0/1\n")
            x = pid.stdout.readline()
        
    # Test CS2
    # print("  - Testing CS2")
    pid.stdin.write("5/1\n")  # CS2+
    x = pid.stdout.readline()

    # Count response "1" of learning behavior
    if x[0] == "1":
        second_half_responses += 1
        response_result = 1
    else:
        response_result = 0
        
    pid.stdin.write("6/1\n")  # CS2-
    x = pid.stdout.readline()
        
    pid.stdin.write("0/1\n")  # Rest
    x = pid.stdout.readline()

    print("  - Fly #{}: CS2 response = {}".format(fly_num + first_half+1, response_result))
        
    # Close pid.stdin and read
    pid.stdin.close()
    print

print

# Calculate PI Value
    
# Calculate PI for first half (CS1)
if first_half > 0:
    first_half_percentage = (first_half_responses * 100.0) / first_half
    pi_first_half = (first_half_percentage - 50.0) * 2.0
else:
    first_half_percentage = 0
    pi_first_half = 0
    
# Calculate PI for second half (CS2)
if second_half > 0:
    second_half_percentage = (second_half_responses * 100.0) / second_half
    pi_second_half = (second_half_percentage - 50.0) * 2.0
else:
    second_half_percentage = 0
    pi_second_half = 0

print("\nCalculating Performance Index (PI) Values")
print("=" * 60)

print("\nFirst Half (CS1 Test) Results:")
print("  - Group size: {}".format(first_half))
print("  - Learning responses (count of '1'): {}".format(first_half_responses))
print("  - Response percentage: {:.1f}%".format(first_half_percentage))
print("  - Performance Index (PI): {:.1f}".format(pi_first_half))

print("\nSecond Half (CS2 Test) Results:")
print("  - Group size: {}".format(second_half))
print("  - Learning responses (count of '1'): {}".format(second_half_responses))
print("  - Response percentage: {:.1f}%".format(second_half_percentage))
print("  - Performance Index (PI): {:.1f}".format(pi_second_half))

# Print Out by comparison
print("\nComparison Results:")
print("=" * 60)
    
print("CS1 (First-order learning) PI: {:.1f}".format(pi_first_half))
print("CS2 (Second-order learning) PI: {:.1f}".format(pi_second_half))



