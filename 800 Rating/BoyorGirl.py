def checkBoyOrGirl():
    # Input: Prompt the user to enter a username and convert it to a set to get distinct characters
    name = len(set(input()))
    
    # Determine the gender based on the number of distinct characters
    if name % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

# Call the function to check the gender
checkBoyOrGirl()
