# custom programming language for fun
import random
import string
import secrets
print("inQuire command line")
print("==================",end="\n")
dosh = 0
items = ["phone"]
mine = ["stone", "iron", "iron", "copper", "copper", "copper", "silver", "silver", "gold"]
saved_vals = {} # dictionary for saved values
cmdlist = ["end - ends the program",
           "roll - emulates d6 die roll (rolls for £)",
           "out - outputs every argument",
           "in - requests an input and outputs it",
           "insave - requests input, outputs, and saves it to argument name",
           "getsave - resolves saved input assigned to argument name",
           "dosh - check your bank account",
           "mine - spend £20 on mining",
           "inventory - check your inventory",
           "sell - sell ALL copper/silver/gold",
           "password - generate a secure password (this command costs £35)"
           ]
flags = [0]
pt = "start" # pt is the command
while pt != "end":
    pt = input("Type a command: ")
    fpt = pt.split(" ",1)[0] # arguments
    if ' ' in pt:
       arg = pt.split(None,1)[1]
    else:
        arg = " "
    if fpt == "roll": # picks number from 1 to 6 and adds that to dosh counter if dosh less than 30
        rollnum = random.randint(1,6)
        print("Roll output:",rollnum)
        if dosh < 30: 
         dosh += rollnum
    if fpt == "out": # outputs argument
        print(arg)
    if fpt == "in": # inputs argument
        value = input(arg+": ")
        print("output: "+value)
    if fpt == "insave": # the arg given is the name of the value. whatever is typed can be accessed...
        value_save = input(arg+": ")
        print("output: "+value_save)
        saved_vals.update({arg:value_save})
    if fpt == "getsave": # ...by typing the argument name of the previous given value
        if arg:
            print(saved_vals[arg])
        else:
            print("No value saved.")
    if fpt == "dosh": # simple; shows the amount of "dosh" you have
        print(dosh)
    if fpt == "mine": # "mines" a random item from the list "mine" and adds to items
        if dosh >= 20:
            dosh -= 20
            x = random.randint(0,len(mine)-1) # picks a random number to "mine" from
            y = mine[x]
            items.append(y)
            print(mine[x], "acquired")
    if fpt == "inventory": # another simple one; shows your items.
        print(items)
    if fpt == "sell": # sells all your copper/silver/gold for different prices
        ac = 0
        for w in items:
            if w == "gold":
             items.remove("gold")
             ac += 48 # technically a profit of 28 is made
            elif w == "silver":
             items.remove("silver")
             ac += 36 # likewise, 16
            elif w == "copper":
             items.remove("copper")
             ac += 24 # and 4
        print("Total profit made: ",ac)
        dosh += ac
    if fpt == "password": # this is the first command that you must use "dosh" to pay for
        if flags[0] == 1: # checks if command has been purchased
            passw = ""
            alphabet = string.ascii_letters + string.digits # populates an assortment of potential chars
            for i in range(12):
             passw += "".join(secrets.choice(alphabet)) # creates the password
            print(passw)
        elif dosh >= 35: # if you have enough money but haven't bought it, you can
            ans = input("Type yes to buy.")
            if ans == "yes":
                flags[0] = 1 # the check will now be passed next time it is run
                print("The command 'password' was bought.")
    if fpt == "help": # prints a list of commands and elaborates further upon each
        for i in range(0,len(cmdlist)):
            print(cmdlist[i])
