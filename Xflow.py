import Flow
import Debate
import os
from colorama import Fore, Back, Style
##This should be a program that handles the flow of the debate. 
##It should be able to handle the flow of the debate, and the flow of the arguments.

print("Welcome to the Debate Flow Manager.")
print("Available Commands:")
print("- To create a new contention: new contention <name>")
print("- To create a new point: new point <text>")
print("- To create a new warrant: new warrant <text>")
print("- To create a new impact: new impact <text>")
print("- To switch pointers: switch <contention_id>.<point_id>")
print("- To exit: exit")

debate = Debate.Debate()
cmd = input(">> ")
while debate.parse(cmd):
    cmd = input(Fore.WHITE + ">> ")

    