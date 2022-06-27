from _socket import getservbyport
from tkinter import *
from socket import getservbyname

# Maks was here

root = Tk()

## Program title ##

title = Label(root, text="Digital Port Number Cheat Sheet")
title.pack()

## Creating a submission box to enter a service ##

subBox = Entry(root)
subBox.pack()
subBox.insert(0, "Enter a Protocol: ")


## Define a function to get the entry from the submission box and use the getservbyname function to find and return the port ##
def onClick():
    service = subBox.get()

    if service.isdigit():
        result = str(getservbyport(service))
    else:
        result = str(getservbyname(service))
    ansLabel = Label(root, text="The port for " + service + " is: " + result)
    ansLabel.pack()

## Creating submission button ##

subButton = Button(root, text="Submit", command=onClick)
subButton.pack()

## End Mainloop ##

root.mainloop()
