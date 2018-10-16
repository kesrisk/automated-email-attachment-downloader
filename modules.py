import os
import shutil
import datetime
import socket
from datetime import datetime, timedelta



def get_extension(filename):
        reversed_filename = filename[::-1]
        n = reversed_filename.find('.')
        ext = reversed_filename[:n]
        ext = ext[::-1]
        return ext


def accepted_day():
    date = datetime.datetime.today().weekday()

    if date == 0:
        accepted_days = ['Mon', 'Sun', 'Sat', 'Fri']
    elif date == 1:
        accepted_days = ['Tue', 'Mon', 'Sun', 'Sat']
    elif date == 2:
        accepted_days = ['Wed', 'Tue', 'Mon', 'Sun']
    elif date == 3:
        accepted_days = ['Thu', 'Wed', 'Tue', 'Mon']
    elif date == 4:
        accepted_days = ['Fri', 'Thu', 'Wed', 'Tue']
    elif date == 5:
        accepted_days = ['Sat', 'Fri', 'Thu', 'Wed']
    elif date == 6:
        accepted_days = ['Sun', 'Sat', 'Fri', 'Thu']
    return accepted_days


def remove_extra_folder(user_directory):        # user_directory to save in particular user_directory
    path = os.path.join(os.getcwd(), 'Email', user_directory)
    files = os.listdir(path)
    accept = accepted_day()
    for date in files:
        if date[:3] in accept:
            # print(date)
            pass
        else:
            directory_path = os.path.join(os.getcwd(), 'Email', user_directory, date)
            move_path = os.path.join(os.getcwd(), 'bin', user_directory)
            if not os.path.exists(move_path):
                os.makedirs(move_path)
            try:
                shutil.move(directory_path, move_path)
            except FileNotFoundError:
                print('file not found')


def get_sender_email_address(email_address):
    email_address = email_address[::-1]
    n = email_address.find(' ')
    email_address = email_address[:n]
    email_address = email_address[::-1]
    email_address = email_address[1:-1]
    # print(email_address)
    return email_address


def get_email_from_user():
    try:
        file = open('email.txt', 'r')
        data = file.read()
        print('files to be feached from these emails \n',data)
    except FileNotFoundError:
        print("File Not Found Please store email.txt file in the root directory")
        end_program = input('press enter to exit')
        exit()
    return data


REMOTE_SERVER = "www.google.com"


def is_connected(hostname):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        print('Connection Established')
        return True
    except:
        print('Internet Not connected, Connect to internet and Try again')
        end_program = input('press enter to exit')
        exit()
    return False
# %timeit is_connected(REMOTE_SERVER)
# > 10 loops, best of 3: 42.2 ms per loop


def get_previous_dates(N):
    # print(datetime.now())
    list1 = []
    for item in range(N):
        date_N_days_ago = datetime.now() - timedelta(days=item)
        date_N_days_ago = date_N_days_ago.strftime('%d-%m-%Y')
        date = date_N_days_ago
        list1.append(date)
    print(list1)
    return list1
