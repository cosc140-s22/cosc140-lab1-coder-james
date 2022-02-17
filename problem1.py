#
# Name: James Cavallo
# Collaborator(s):
#

def main():
    totalSeconds = int(input("How many seconds? "))
    if totalSeconds < 0:
        print("invalid input")
        return
    
    days = totalSeconds // 86400
    remainingSeconds = totalSeconds - (days * 86400)
    hours = remainingSeconds // 3600
    remainingSeconds = remainingSeconds - (hours * 3600)
    minutes =  remainingSeconds // 60
    seconds = remainingSeconds - (minutes * 60)

    print(str(totalSeconds) + " seconds is equivalent to " +  str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")

if __name__ == '__main__':
    main()

