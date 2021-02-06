import imaplib
import email
from email.header import decode_header
import os
from bs4 import BeautifulSoup
import re
import regex
import csv


# account credentials
username = "your-email@gmail.com"
password = " enter app password here"



# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)

print(" ")
print("login successful ma buddy!")
print(" ")



status, messages = imap.select("INBOX")

if status == "OK":
    print("Inbox accessed")
    print(" ")
else:
    print("Oops. Couldn't access inbox. Quitting...")
    quit()

status_2, data = imap.search(None, '(FROM "service@paypal.co.uk" SUBJECT "just paid for your invoice" UNSEEN)')

id_list = data[0].split()

#I commented out this block of code after running it the first time. See Readme document.
#with open("payments.csv", "a", newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(["Date", "Name of Payer", "Amount Paid", "Currency", "Invoice Number", "Payment Platform"])
#    file.close()

#for email ids in range
for i in id_list:
    res, msg = imap.fetch(i, '(RFC822)')
    message = email.message_from_bytes(msg[0][1])
    unformatted_date_1 = message["date"]
    unformatted_date_2 = regex.search(r'(?<=Mon, |Tue, |Wed, |Thu, |Fri, |Sat, |Sun, )[0-9a-zA-Z ]+', unformatted_date_1).group(0)
    date = unformatted_date_2[:-3]
    message_payload = message.get_payload(decode=True)
    soup = BeautifulSoup(message_payload, "lxml")
    message_in_plain_text = soup.get_text()
    #print(message_in_plain_text)
    name_of_payer = re.search(r'[a-zA-z0-9- ]+(?= just paid for your invoice)', message_in_plain_text).group(0)
    invoice_number = re.search(r'(?<=just paid for your invoice )[0-9]+', message_in_plain_text).group(0)
    amount_paid = re.search(r'(?<=You received a )[$0-9.]+', message_in_plain_text).group(0)
    currency = regex.search(r'(?<=You received a [$0-9.]+ )[A-Za-z]+', message_in_plain_text).group(0)
    platform = "PayPal"
   
    print("I'm now writing the extracted information to the file.")
    print(" ")
    with open("payments.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, name_of_payer, amount_paid, currency, invoice_number, platform])
        file.close()
print("All done now! You may check my work by opening the payments.csv.\n \nI hope you like my work! Bye now!\n \nYou're richhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!\n")

print ("""\
      _.-'''''-._
    .'  _     _  '.
  /   (o)   (o)   \
  |                 |
  |  \           /  |
   \  '.       .'  /
    '.  `'---'`  .'
      '-._____.-' \n""")






#Sources
#https://stackoverflow.com/questions/16206380/python-beautifulsoup-how-to-remove-all-tags-from-an-element
#https://stackoverflow.com/questions/14694482/converting-html-to-text-with-python
#https://docs.python.org/3/library/email.parser.html
#https://stackoverflow.com/questions/3449220/how-do-i-recieve-a-html-email-as-a-regular-text
#https://docs.python.org/3/library/email.compat32-message.html?highlight=walk#email.message.Message.is_multipart
#https://docs.python.org/3/library/imaplib.html
#https://tools.ietf.org/html/rfc3501.html#page-49
#https://pymotw.com/2/imaplib/
#https://www.thepythoncode.com/article/reading-emails-in-python
#https://codehandbook.org/how-to-read-email-from-gmail-using-python/
#https://www.devdungeon.com/content/read-and-send-email-python
#https://stackoverflow.com/questions/18493677/how-do-i-return-a-string-from-a-regex-match-in-python
#https://www.dataquest.io/blog/regex-cheatsheet/
#https://stackoverflow.com/questions/20089922/python-regex-engine-look-behind-requires-fixed-width-pattern-error
#https://www.programiz.com/python-programming/writing-csv-files
#https://www.asciiart.eu/computers/smileys
#https://www.asciiart.eu/computers/smileys
#https://stackoverflow.com/questions/23623288/print-full-ascii-art
