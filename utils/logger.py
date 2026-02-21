import datetime
def log(message: str):
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {message}")
