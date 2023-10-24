import threading


def start_thread(function):
    monitor_thread = threading.Thread(target=function)
    monitor_thread.setDaemon(True)
    monitor_thread.start()
