import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from os import listdir
from os.path import isfile, join
import re
import logging
import os
#Import configuration parameters
import config as c

    


#Open the log file
logger = logging.getLogger('file_sender')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('/tmp/fileserver.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)

try:
    #Scan the folder

    files = [f for f in listdir(c.path) if isfile(join(c.path, f))]
    logger.info("Found "+str(len(files)) + " files")


    #Connect to the server
    conn=smtplib.SMTP(c.server+":"+str(c.port))
    conn.ehlo()
    if c.tls:
        conn.starttls()
    conn.login(c.email,c.password)

    #Build the message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = c.subject
    msg['From']    = ""+c.sender+" <"+c.email+">"
    msg['To']      = c.receiver
    msg.attach(MIMEText(c.body))

    #Add attachments
    for f in files:
            with open(join(c.path,f), "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=f
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % f
            msg.attach(part)

    #Send the email
    conn.sendmail(c.email, c.receiver, msg.as_string())
    conn.close()

    #Log email sent
    logger.info("Email sent correctly")

    #Delete (1) Move(2) or nothing (3)

    for f in files:
        if c.execution_mode==1:
            os.remove(c.pathf)
            logger.info("File " + f + " deleted")
        elif c.execution_mode==2:
            os.rename(join(c.path,f), join(c.move_to,f))
            logger.info("File " + f + " moved to "+ c.move_to)

    logger.info("Script finished successfully!")
except Exception as e:
    logger.fatal(e, exc_info=True)
    
