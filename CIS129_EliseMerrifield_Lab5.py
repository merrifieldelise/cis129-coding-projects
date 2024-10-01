#Elise Merrifield, 10/1/2024, This code counts the number of bottels collected over 7 days and
# calcullates the amount given for them
#Lab 5 The Bottle Return Program

#Step 1: Declare variables
nbr_of_days = 7
total_bottles = 0
total_payout = 0 #calculated by total_bottles * 0.10
today_bottles = 0
counter = 0
keep_going = "y"

#Step 2: Loop to run program agin
while keep_going == "y" and counter < nbr_of_days:
    #step 3: code set values of variables
    #count number of days
    counter += 1
    #get input about bottles
    today_bottles = int(input("How many bottles were gathered today?\n"))
    #set program to end
    if counter >= nbr_of_days:
        #set value of total_bottles
        total_bottles += today_bottles
        #set value of total_payout
        total_payout = total_bottles * 0.10
        #code to print totals
        print(f"Total Bottles For Week: {total_bottles}")
        print(f"Total Payout For Week: ${total_payout:.2f}")
        keep_going = input("Do you want to enter another week’s worth of data?(Enter y or n)\n")
        #have counter and total bottles reset for reruning code
        counter = 0
        total_bottles = 0
    #set to end if not repeated
    elif keep_going != "y":
        break
