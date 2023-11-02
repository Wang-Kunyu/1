import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = 'bob'
socket, aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)
#print('Connected with Alice!')

os.chdir(BUFFER_DIR)
os.rename(BUFFER_FILE_NAME, 'buffer2')
#print(BUFFER_DIR)
#print(BUFFER_FILE_NAME)

dialog2 = Dialog('print')
player2 = 'alice'
socket2, aes2 = setup(player2, BUFFER_DIR, BUFFER_FILE_NAME)
#print('Connected with Alice!')

received = receive_and_decrypt(aes2, socket2)

if sys.argv[1] == '--relay':
    relay = True
    break_heart = False
    custom = False
elif sys.argv[1] == '--break-heart':
    relay = False
    break_heart = True
    custom = False
else:
    relay = False
    break_heart = False
    custom = True

if relay:
    to_send = received
elif break_heart:
    to_send = BAD_MSG['bob']
else:
    dialog.prompt('Please input message...')
    to_send = input()
    
encrypt_and_send(to_send, aes, socket)
received2 =  receive_and_decrypt(aes, socket)

tear_down(socket, BUFFER_DIR, BUFFER_FILE_NAME)
os.chdir(BUFFER_DIR)
os.rename('buffer2', BUFFER_FILE_NAME)

if relay:
    to_send2 = received2
elif break_heart:
    to_send2 = BAD_MSG['alice']
else:
    dialog.prompt('Please input message...')
    to_send2 = input()

encrypt_and_send(to_send2, aes2, socket2)

tear_down(socket2, BUFFER_DIR, BUFFER_FILE_NAME)



