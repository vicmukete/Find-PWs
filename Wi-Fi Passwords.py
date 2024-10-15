import subprocess
import os
import sys

# create a file
password_file = open("Master's Passwords.txt", "w")
password_file.write("Here are the requested passwords:\n\n")
password_file.close()

# Lists
wifi_files = []
wifi_name = []
wifi_pw = []

# use python ot execute a windows command
# i assume this gives us our files, but where does the naming convention come from?
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

# Grab current directory
path = os.getcwd()

# Main.py
for filename in os.listdir(path):
    if '.xml' in filename:
        wifi_files.append(filename)


for i in wifi_files:
    with open(i, 'r') as f:
        for line in f.readlines():
            if 'name' in line:
                stripped = line.strip()
                front = stripped[6:]
                back = front[:-7]
                wifi_name.append(back)
            if 'keyMaterial' in line:
                stripped = line.strip()
                front = stripped[13:]
                back = front[:-14]
                wifi_pw.append(back)

with open("Master's Passwords.txt", 'w') as output_file:
    wifi_name = set(wifi_name)
    for x, y in zip(wifi_name, wifi_pw):
        output_file.write("SSID: " + x + "\nPassword: " + y + '\n\n')

print("Passwords have been saved Master.")
print(f"The wifi names are: {wifi_name}")
print(f"The wifi passwords are: {wifi_pw}")
print(os.listdir(path))
