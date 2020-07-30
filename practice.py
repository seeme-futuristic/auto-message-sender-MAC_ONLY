import os
import keyboard
import time


##### THE CODE #####


#This is the person that you want to text
recipient = input("What is the phone number you would like to text?: ")

#This is what you want to say to the chosen person
message = input("What would you like to say?: ")

#This is how many times you want to send the message...use this wisely
amount_ = int(input("How many times would you like to send this message?: "))

#Opens imessage app on your Mac system
def open_messages():
    os.system("open /System/Applications/Messages.app")

#This function creates a new message and brings the cursor into the text field where the message will be written
def setup():
    keyboard.press_and_release('cmd+n')
    time.sleep(1.5)
    keyboard.write(recipient)
    time.sleep(.5)
    keyboard.press_and_release('return')

#Goes through the action of writing and sending the message
def send_message():
    keyboard.write(message)
    time.sleep(0.5)
    keyboard.press_and_release('return')

#This will send the message as many times as you requested
def repeater(amount_):
    for i in range(0, amount_):
        send_message()

####################

recipient
message
amount_
open_messages()
time.sleep(1)
setup()
time.sleep(1)
repeater(amount_)
