# -*- coding: utf-8 -*-
from imapclient import IMAPClient
from email import message_from_bytes
from email.header import decode_header
from email.utils import parsedate_to_datetime,parseaddr
import ssl
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
    
    port = 993  # Change to the correct port for IMAPS
    context = ssl.create_default_context()  # Use the default context for SSL/TLS
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Disable certificate verification (not recommended for production)
    try:
        client=IMAPClient(hinet_server,port=port,ssl=True,ssl_context=context)   
        client.login(hinet_user, hinet_password)
        print("Hinet connection successful")
    except Exception as e:
        print(f"Connection failed: {e}") 
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
    
    port = 993  # Change to the correct port for IMAPS
    context = ssl.create_default_context()  # Use the default context for SSL/TLS
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Disable certificate verification (not recommended for production)
    try:
        client=IMAPClient(hinet_server,port=port,ssl=True,ssl_context=context)   
        client.login(hinet_user, hinet_password)
        print("Hinet connection successful")
    except Exception as e:
        print(f"Connection failed: {e}")
        

if __name__ == "__main__":
    test_conect_test()