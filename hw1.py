#converts hours to minutes
def hrsToMins(hrs):
    return hrs * 60
#converts either hours to minutes or minutes to hours
def timeConverter(unit,time):
    if unit == "hours":
        return time * 60
    elif unit == "minutes":
        return time / 60
    else:
        return "invalid unit"
#counts the amount of letters in a word
def letterCounter(word):
    nums = 0
    for l in word:
        nums += 1
    return nums
#to choose which program to run
program = input("select program 1, 2, or 3: ")
#for hours to minutes conversion
if program == "1":
    print(hrsToMins(int(input("enter hours: "))))
#for hours to minutes or minutes to hours
elif program == "2":
    print(timeConverter(input("enter unit: "), int(input("enter time: "))))
#for counting letters in word
elif program == "3":
    print(letterCounter(input("enter word: ")))
#crude failsafe
else:
    print("invalid program selection")