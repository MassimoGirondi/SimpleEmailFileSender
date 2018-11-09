
#Sender details, server configuration
email="email@server.com"
password="password"
server="smtp.server.com"
port=587
tls=True


#Receiver
receiver="receiver@domain.com"

#Subject of the email
subject="Automatic file sender"

#Sender (seen in email)
sender="Your automatically file sender"

#Body of the email
body='''Hi,
here there are your files.
Have a nice day!
Your faithful Python program.
'''

#Path of your folder
path="/home/user/documents"


#Delete (1), Move(2) or do nothing (3) to files after sending?
execution_mode=2
move_to="/home/user/documents/old"

#Path of log
log_path="/home/user/filesender.log"

