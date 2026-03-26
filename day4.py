import os
import platform
import datetime
import getpass

def system_info():
    print("---- SYSTEM INFO ----")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Date & Time: {now}")

    hostname = platform.node()
    print(f"Hostname: {hostname}")

    python_version = platform.python_version()
    print(f"Python Version: {python_version}")

    user = getpass.getuser()
    print(f"Current User: {user}")

    files = os.listdir(".")
    print("Files in Directory:")
    for f in files:
        print(f"- {f}")
    print(f"Total Files: {len(files)}")

    user_input = input("Enter a message: ")
    print(f"You entered: {user_input}")

if __name__ == "__main__":
    system_info()




