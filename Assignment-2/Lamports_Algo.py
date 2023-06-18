import random

N = 4
MAX_CRITICAL_SECTION_TIME = 3

class Process:
    def __init__(self, pid=-1, request_time=-1, time_in_cs=-1):
        self.pid = pid
        self.request_time = request_time
        self.time_in_cs = time_in_cs
        
    def get_request_time(self):
        return self.request_time
    
    def get_time_in_cs(self):
        return self.time_in_cs
    
    def reduce_time_in_cs(self):
        self.time_in_cs -= 1

global_clock = 0
request_queue = []
wait_queue = []

for i in range(10):
    proc = random.randint(0, N-1)
    time = random.randint(1, MAX_CRITICAL_SECTION_TIME)
    request_queue.append(Process(proc, i, time))

is_in_cs = False
process_in_cs = Process()

while request_queue or wait_queue:
    if request_queue:
        request = request_queue[0]
        print(f"Process {request.get_request_time()} requests critical section at {request.get_request_time()} for time {request.get_time_in_cs()} units")
        request_queue.pop(0)
        wait_queue.append(request)
    if is_in_cs:
        if process_in_cs.get_time_in_cs() == 0:
            print(f"Process {process_in_cs.get_request_time()} exits critical section at {global_clock}")
            is_in_cs = False
            if wait_queue:
                request = wait_queue[0]
                wait_queue.pop(0)
                process_in_cs = request
                is_in_cs = True
                print(f"Process {request.get_request_time()} enters critical section at {global_clock}")
        else:
            process_in_cs.reduce_time_in_cs()
    else:
        if wait_queue:
            request = wait_queue[0]
            wait_queue.pop(0)
            process_in_cs = request
            is_in_cs = True
            print(f"Process {request.get_request_time()} enters critical section at {global_clock}")
    global_clock += 1