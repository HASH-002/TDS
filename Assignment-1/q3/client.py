import rpyc
from threading import Thread
import time
import sys

Capacity = 0
net = None
input_var = None
user_name = None

def myprint(message):
    print(message)

def checkAndPrint(delay, dont):
    global Capacity
    global net
    global user_name
    global input_var
    while True:
        Size = conn.root.replyLength(1)
        if input_var == "exit":
            break
        while Capacity < Size:
            net = conn.root.replyWith(Capacity)
            Capacity += 1
            print(net)


conn = rpyc.connect('localhost', 18853)
conn.root.response(myprint)

user_name = input("Enter your username: ")
print("Enter 'exit' to quit chat")
conn.root.serverPrint(user_name)
reach = conn.root.replyLength(1)

try:
    t = Thread(target=checkAndPrint, args=(0, 0))
    t.start()

    while True:
        input_var = input()
        if input_var == "exit":
            time.sleep(1)
            input_var = user_name + " has left the conversation"
            conn.root.response(myprint)
            conn.root.serverPrintMessage(input_var)
            conn.root.serverExit(user_name)
            break
        Capacity += 1
        input_var = user_name + ":" + input_var
        conn.root.response(myprint)
        conn.root.serverPrintMessage(input_var)

except Exception as errtxt:
    print("You left the chat")
