# -*- coding: utf-8 -*-
from imapclient import IMAPClient
from email import message_from_bytes
from email.header import decode_header
from email.utils import parsedate_to_datetime,parseaddr

def gmailserver_str():
    gmail_server = 'imap.gmail.com'
    gmail_user = 'cing5417@gmail.com'
    gmail_password = 'xdus pmxb gpkv zbtb'
    return[ gmail_server, gmail_user, gmail_password]
def hinetserver_str():
    hinethinet_server = 'msa.hinet.net'
    hinet_user = 'fuxi.su'
    hinet_password = '!Tzj012589'
    return[ hinethinet_server, hinet_user, hinet_password]

def con2mailserver(server, user, password):
    with IMAPClient(server) as client:
        client.login(user, password)
        return client
def con2gmailserver():
    
    gmail_server, gmail_user, gmail_password = gmailserver_str()
    client = IMAPClient(gmail_server)
    client.login(gmail_user, gmail_password)
    return client
def con2hinetserver():
    hinet_server,hinet_user,hinet_password = hinetserver_str()
    client=IMAPClient(hinet_server)   
    client.login(hinet_user, hinet_password)
    return client    
def test_conect_test():
    # Test with Gmail server
    gmail_server, gmail_user, gmail_password = gmailserver_str()
    try:
        client = con2mailserver(gmail_server, gmail_user, gmail_password)
        print("Gmail connection successful")
        
    except Exception as e:
        print(f"Gmail connection failed: {e}")

    # Test with Hinet server
    hinet_server, hinet_user, hinet_password = hinetserver_str()
    try:
        client = con2mailserver(hinet_server, hinet_user, hinet_password)
        print("Hinet connection successful")
        
    except Exception as e:
        print(f"Hinet connection failed: {e}")

if __name__ == "__main__":
    test_conect_test()