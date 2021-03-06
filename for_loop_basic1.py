# 1. Basic - Print all integers from 0 to 150.
for count in range(151):
    print(count)

#  testing a while loop
count = 0
while count <= 150:
    print(count)
    count += 1

    
# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for num in range(5, 1001):
    if num % 5 == 0:
        print(num)


# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)


# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for num in range(0, 500001):
    if num % 2 != 0:
        sum += num
print(sum)


# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    if i >= 0:
        print(i)

        
# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexibleCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        if i % mult == 0:
            print(i)

flexibleCounter(2, 9, 3)
