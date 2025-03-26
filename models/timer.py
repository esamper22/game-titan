import time


class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.seconds = 0
    
    def get_time(self):
        self.seconds = time.time() - self.start_time
        return self.seconds

    def compare_time(self, sec=1):
        return self.get_time() > sec
    
    def reset(self):
        self.start_time = time.time()