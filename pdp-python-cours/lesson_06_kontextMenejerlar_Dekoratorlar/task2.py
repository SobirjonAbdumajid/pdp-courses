import datetime

class log:
    def __enter__(self):
        self.start_time = datetime.datetime.now()
        print(f"- context manager opened at {self.start_time.strftime('%H:%M:%S')}")
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = datetime.datetime.now()
        print(f"- context manager closed at {self.end_time.strftime('%H:%M:%S')}")

with log():
    print("hello")