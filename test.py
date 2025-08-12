from datetime import datetime

def decorator(func):
    start_time = datetime.now()
    func()
    end_time = datetime.now()

    diff = end_time - start_time
    print(f"Время выполнения (ms): {(diff.microseconds)}")

@decorator
def sum_number(a, b):
    return a + b

sum_number(100, 20)
