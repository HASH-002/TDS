import rpyc
connection = rpyc.connect('localhost', 18852)

current_time = connection.root.current_date_and_time()
print("Current date and time is ",current_time)