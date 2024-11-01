import subprocess
import os

# import sys

# create a file
password_file = open("Master's Passwords.txt", "w")
password_file.write("Here are the requested passwords:\n\n")
password_file.close()

# Lists to populate
wifi_files = []
wifi_name = []
wifi_pw = []

# use python ot execute a windows command
# i assume this gives us our files, but where does the naming convention come from?
subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

# Grab current directory
path = os.getcwd()


# function to get a specific line number to obtain the ssid
def read_specific_line(file_path, line_number):
    with open(file_path, 'r') as file:
        for each_line in range(line_number - 1):
            file.readline()  # Skip lines until you reach the desired one
        return file.readline()


# Main.py
for filename in os.listdir(path):
    if 'Wi-Fi' in filename:
        wifi_files.append(filename)

wifi_credentials = []
for each_file in wifi_files:
    ssid = None
    password = None

    with open(each_file, 'r') as f:
        for rows in f.readlines():

            # strip the line for only the ssid
            if 'name' in rows:
                line = read_specific_line(each_file, 3)  # Read the 3rd line
                stripped = line.strip()
                front = stripped[6:]
                back = front[:-7]
                ssid = back

            # strip the line for only the passwords
            if 'keyMaterial' in rows:
                stripped = rows.strip()
                front = stripped[13:]
                back = front[:-14]
                password = back

        if ssid:
            wifi_credentials.append((ssid, password if password else "No Password"))

with open("Master's Passwords.txt", 'w') as output_file:
    for ssid, password in wifi_credentials:
        output_file.write(f"SSID: {ssid}\nPassword: {password}\n\n")


print("Passwords have been saved Master.")
print()
print(f"wifi_credentials: {wifi_credentials}")
print(len(wifi_credentials))
print()
print(os.listdir(path))
print(len(os.listdir(path)))
print()
