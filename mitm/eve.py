import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = 'bob'
socket, aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)
#print('Connected with Alice!')

dialog2 = Dialog('print')
player2 = 'alice'
socket2, aes2 = setup(player2, BUFFER_DIR, BUFFER_FILE_NAME)
#print('Connected with Alice!')

received = receive_and_decrypt(aes2, socket2)

relay = True
break_heart = False
custom = False

if relay:
    to_send = received
elif break_heart:
    to_send = BAD_MSG['bob']
else:
    CUSTOM_CHAT = True
    
encrypt_and_send(to_send, aes, socket)
received2 =  receive_and_decrypt(aes, socket)

if relay:
    to_send2 = received2
elif break_heart:
    to_send2 = BAD_MSG['alice']
else:
    CUSTOM_CHAT = True

encrypt_and_send(to_send2, aes2, socket2)

tear_down(socket, BUFFER_DIR, BUFFER_FILE_NAME)
tear_down(socket2, BUFFER_DIR, BUFFER_FILE_NAME)

