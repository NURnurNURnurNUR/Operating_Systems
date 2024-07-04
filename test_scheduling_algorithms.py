import unittest
from process import Process
from memory_manager import MemoryManager
from helper_functions import generate_random_processes
from fcfs import fcfs
from srtf import srtf
from round_robin import round_robin

class TestSchedulingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.num_processes = 5
        self.memory_size = 1000
        self.time_quanta = 2

    def test_fcfs(self):
        process_list = generate_random_processes(self.num_processes)
        memory_manager = MemoryManager(self.memory_size)
        fcfs(process_list, memory_manager)

    def test_srtf(self):
        process_list = generate_random_processes(self.num_processes)
        memory_manager = MemoryManager(self.memory_size)
        srtf(process_list, memory_manager)

    def test_round_robin(self):
        process_list = generate_random_processes(self.num_processes)
        memory_manager = MemoryManager(self.memory_size)
        round_robin(process_list, memory_manager, self.time_quanta)

if __name__ == "__main__":
    unittest.main()
