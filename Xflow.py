import Flow
import Debate
import os
from colorama import Fore, Back, Style
##This should be a program that handles the flow of the debate. 
##It should be able to handle the flow of the debate, and the flow of the arguments.

debate = Debate.Debate()
cmd = input(">> ")
while debate.parse(cmd):
    cmd = input(Fore.WHITE+">> ")
    
    