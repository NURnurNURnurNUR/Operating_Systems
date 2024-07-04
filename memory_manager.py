class MemoryManager:
    def __init__(self, size):
        self.size = size
        self.memory = [0] * size
        self.allocated_processes = {}

    def first_fit_allocate(self, process):
        start = 0
        while start < self.size:
            end = start
            while end < self.size and self.memory[end] == 0:
                end += 1
            if end - start >= process.memory:
                for i in range(start, start + process.memory):
                    self.memory[i] = 1
                self.allocated_processes[process.pid] = (start, process.memory)
                return True
            start = end + 1
        return False

    def deallocate_memory(self, pid):
        if pid in self.allocated_processes:
            start, size = self.allocated_processes.pop(pid)
            for i in range(start, start + size):
                self.memory[i] = 0

    def __repr__(self):
        return f"MemoryManager(size={self.size}, memory={self.memory}, allocated_processes={self.allocated_processes})"
