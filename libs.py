import socket

    
def welcome_message():
    desktop = socket.gethostname()
    line = "-" * (len(desktop) + 4)
    print(line)
    print(f"- {desktop} -")
    print(line)