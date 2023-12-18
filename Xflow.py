import Flow
##This should be a program that handles the flow of the debate. 
##It should be able to handle the flow of the debate, and the flow of the arguments.

contentions = []
while True:
    cmd = input(">> ")
    if cmd == "exit":
        break
    elif "new" in cmd:
        item = cmd.split(" ")
        if item[1] == "contention":
            contentions.append(Flow.Contention(item[2]))
            contentions[-1].printContention()
        