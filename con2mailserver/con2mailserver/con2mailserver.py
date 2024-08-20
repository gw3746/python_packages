# -*- coding: utf-8 -*-
from imapclient import IMAPClient
from email import message_from_bytes
from email.header import decode_header
from email.utils import parsedate_to_datetime,parseaddr

def con2gmailserver():
    gmail_server = 'imap.gmail.com'
    gmail_user = 'cing5417@gmail.com'
    gmail_password = 'xdus pmxb gpkv zbtb'
    return[ gmail_server, gmail_user, gmail_password]
def con2hinetserver():
    hinethinet_server = 'msa.hinet.net'
    hinet_user = 'fuxi.su'
    hinet_password = '!Tzj012589'
    return[ hinethinet_server, hinet_user, hinet_password]

def con2mailserver(server, user, password):
    with IMAPClient(server) as client:
        client.login(user, password)
        return client
    
def test_conect_test():
    # Test with Gmail server
    gmail_server, gmail_user, gmail_password = con2gmailserver()
    try:
        client = con2mailserver(gmail_server, gmail_user, gmail_password)
        print("Gmail connection successful")
        
    except Exception as e:
        print(f"Gmail connection failed: {e}")

    # Test with Hinet server
    hinet_server, hinet_user, hinet_password = con2hinetserver()
    try:
        client = con2mailserver(hinet_server, hinet_user, hinet_password)
        print("Hinet connection successful")
        
    except Exception as e:
        print(f"Hinet connection failed: {e}")

if __name__ == "__main__":
    test_conect_test()