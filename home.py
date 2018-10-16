import email
import imaplib   #imaplib
import os
import re
import modules
import dateutil.parser
import getpass

modules.is_connected('www.googe.com')
print('processing')

# username = 'shivu.kesri@gmail.com'
# password = ''
username = input('Enter Email: ')
password = getpass.getpass('Enter Password: ')
# password = input('Enter Pass: ')
# program_to_run = input("press 1 to download all file, 2 to download file from given email, 3 to download file except the given file: ")
no_days = 4
print('Username and Password submitted sucessfully')
user_directory = re.sub('[^a-zA-Z0-9]', '', username)
mail = imaplib.IMAP4_SSL("imap.gmail.com")


try:
    mail.login(username,password)                               # login to gmail
    print('Login Successful!')
except:
    print('Invalid credentials')                                 # login failed
    end_program = input('press enter to exit')
    exit()
email_from_user = modules.get_email_from_user()                   # get email from which file is fetched from email
mail.select("inbox")                                              # select gmail inbox for data fetch
result, data = mail.uid('search', None, "ALL")                    # fetch all inbox email location
inbox_list_item = data[0].split()                                 # split inbox data into list list will contain email from oldest to latest file
inbox_list_item = inbox_list_item[::-1]                           # reverse list to get latest to oldest email
for item in inbox_list_item:                                      # loop to process all the email of inbox
    result2, email_data = mail.uid('fetch', item, "(RFC822)")     # fetch data from email location
    raw_email = email_data[0][1].decode("utf-8")                  # decode email data
    email_message = email.message_from_string(raw_email)          # get email message from string
    sender = email_message['from']                                # email sender details
    sender_email_address = modules.get_sender_email_address(sender)      # extract email of sender from sender
    email_from = re.sub('[^ a-zA-Z0-9]', '',sender)                 # remove special signs for the folder name
    email_date = email_message['date']                              # remove special signs for the folder name
    print(email_date)
    email_date = dateutil.parser.parse(email_date)                  # parse email date from email recieved
    email_date = email_date.strftime('%d-%m-%Y')                    # convert date to dd-mm-yyyy format
    print(email_date)                                               # print email date
    email_subject = email_message['subject']
    print(email_from_user)
    print(sender_email_address)
    # get subject of email
    accepted_dates = modules.get_previous_dates(no_days)            # list of days through which mail is to b pulled
    for part in email_message.walk():                               # loop to walk into directory of email inbox
        if part.get_content_maintype() == "multipart":              # if content_maintype = multipart
            continue
        filename = part.get_filename()                              # fetch filename of the attached file
        content_type = part.get_content_type()                      # get content type ie file extension
        if email_date in accepted_dates:                            # if email eccepted


            if sender_email_address in email_from_user:

                print('email accepted')
                if filename:
                    ext = modules.get_extension(filename)
                    acceptable_ext = ['xls', 'xlsx', 'csv']
                    #if ext in acceptable_ext:
                    save_path = os.path.join(os.getcwd(), 'Email', user_directory, email_date, email_from)
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
                    with open(os.path.join(save_path, filename), 'wb') as fp:
                        fp.write(part.get_payload(decode=True))
                        print('write sucessful')
        else:
            end_program = input('press enter to exit')
            exit()
    # if email_day not in accepted_day:
    #     break
# remove_extra_data = modules.remove_extra_folder(user_directory)

end_program = input('press enter to exit')


