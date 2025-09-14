import os
import time
import requests

avica_file = r"C:\ProgramData\Avica\id.ini"
avica_dir = os.path.dirname(avica_file)

print(f"Checking if directory exists: {os.path.exists(avica_dir)}")
if os.path.exists(avica_dir):
    print(f"Files in directory: {os.listdir(avica_dir)}")
else:
    print("Directory not found!")

timeout = time.time() + 120  # 2 minutes timeout
while not os.path.exists(avica_file):
    if time.time() > timeout:
        print("Timeout: Avica ID file not found.")
        exit(1)
    print("Waiting for Avica ID file...")
    time.sleep(5)

print("Uploading ID file to GoFile...")
with open(avica_file, "rb") as f:
    files = {"file": f}
    response = requests.post("https://store1.gofile.io/uploadFile", files=files)

if response.status_code == 200:
    link = response.json()['data']['downloadPage']
    print(f"GoFile Link: {link}")
else:
    print("Failed to upload to GoFile")
