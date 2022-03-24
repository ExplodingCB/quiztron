import os
import time
import timeit
import ctypes
import json
import discord_webhook

#webhook


#config

testname ="TestName"
#this is the allowed people
usernames = ["p1","p2","p3","p4","p5"]

# vars

#Below is the verification key
token = "dev"

#DO NOT EDIT

active = 1
pts = 0
StartTime = 0
EndTime = 0
#allowed names


# credits

print("Created by Xernar & ExplodingCB")

#PYTHONWEBHOOK


#verify menu
verify = input("Please enter your verification key:  ")

if verify == token:
    g = input("Enter your username for authentication: ")
    if g in usernames:


        print("You have been authenticated!")
        print("Welcome to your testing session we have designed this ecosystem of software to prevent against cheating and falsifying answers on tests. Your session has began. YOU ARE BEING SCORED")
        active = 2


if active == 1:
    print("Authentication failed;  unknown or unwanted person please contact developers.")
    I = input("Press anything to continue...")
    quit()



#Question 1 start


#quizpy
print("Acceptable responses")
print("A. 1")
print("B. 2")
print("C. 3")
print("D. 4")
q1 = input("What is 2 + 2: ")
if q1 == "D":
   pts = pts + 1
else:
    pts = pts - 1


#question 1 end


#QUESTION 2 START



print("Acceptable responses")
print("A. y=mx-b")
print("B. y=mx+b")
print("C. b=mx+y")
print("D. mx=b+y")
q2 = input("What is the point slope formula?: ")
if q2 == "B":
   pts = pts + 1
else:
    pts = pts - 1



#QUESTION 3 END


endtest = input("Press any key to end your test...")

print("Your final score is: ")
print(pts)

if pts < 0:
    print("You got 0%")

if pts == 0:
    print("You got 50%")

if pts > 0:
    print("You got 100%")

quittest = input("Press any key to EXIT your test... This action is final your score has been finalized.")

#webhook
from discord_webhook import DiscordWebhook
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/956391347525386250/ysIXnmQ-kHIM3fQvhJjTwB1mWBktl2xasuLJxnHbi5zmg0Erbkpokajh6poHP1y7EjTc', content= " Test Name: " +testname+ " Person taking the test: "+g+" scored a  " +str(pts))
response = webhook.execute()

#stop
quit()

# ("-''-/").___..--''"-.
 # `6 6  )   -.  (     ).-.__.)
 # (_Y_.)'  ._   )  . `. ``-..-'
  #  ..`--'..-/  /--'_.'
  # ((((.-''  ((((.'  (((.-'