import os
import requests
import time
from telegraph import upload_file

# Set the Avica ID and password file (create this file during installation)
avica_file = r"C:\ProgramData\Avica\id.ini"

# Wait until the file exists, with timeout
timeout = time.time() + 120  # 2 minutes timeout
while not os.path.exists(avica_file):
    if time.time() > timeout:
        print("Timeout: Avica ID file not found.")  # Emoji removed here
        exit(1)
    time.sleep(5)

# Upload to GoFile
print("Uploading ID file to GoFile...")
with open(avica_file, "rb") as f:
    files = {"file": f}
    response = requests.post("https://store1.gofile.io/uploadFile", files=files)

if response.status_code == 200:
    link = response.json()['data']['downloadPage']
    print(f"GoFile Link: {link}")
else:
    print("Failed to upload to GoFile")
