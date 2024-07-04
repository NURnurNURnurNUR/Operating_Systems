class Process:
    def __init__(self, pid, arrival_time, burst_time, memory):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.memory = memory
