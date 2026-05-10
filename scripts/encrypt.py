import os

def encrypt_disk(disk):
    print("Simulated encryption for lab safety")
    print(f"Disk: {disk}")
    print("Steps: LUKS format → open → mount")

encrypt_disk("/dev/sda1")
