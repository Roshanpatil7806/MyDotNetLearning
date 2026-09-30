import threading
import time

def download_policy():
    print("Downloading policy...")
    time.sleep(3)
    print("Policy downloaded")

def send_email():
    print("Sending email...")
    time.sleep(2)
    print("Email sent")

t1 = threading.Thread(target=download_policy)
t2 = threading.Thread(target=send_email)
# start() method is used to start the execution of a thread.
t1.start()
t2.start()

#we use join() to make the main program wait until a thread finishes its work.
t1.join()
t2.join()

print("All tasks completed")
