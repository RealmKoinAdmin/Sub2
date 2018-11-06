"""
EthFlayer.py
Skrypt
Copyright (C) 2018 Skryptek
 
This program is for informational testing purposes ONLY.
@ Dev Needs Pickle Login / Save / Load Features
@ Dev Needs Internal Database For Seed Duplicates.
"""
print(''' Welcome To EthFlayer Please Be Patient While I Import The Following Modules And Packages.''')
################ Import Section #############################################
global pickle_db
global bitcoin_highvalue_list
global First_Display_Targets
First_Display_Targets = False
pickle_db = False
try:
 print('Attempting To Import [os] Module.')
 import os
except Exception as bad_os_mod:
 print('Error Importing [os] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_os_mod))
 exit()

try:
 print('Attempting To Import [argparse] Module.')
 import argparse
except Exception as bad_argparse_mod:
 print('Error Importing [argparse] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_argparse_mod))
 exit()

try:
 print('Attempting To Import [binascii] Module.')
 import binascii
except Exception as bad_binascii_mod:
 print('Error Importing [binascii] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_binascii_mod))
 exit()

try:
 print('Attempting To Import [sha3] Module.')
 import sha3
except Exception as bad_sha3_mod:
 print('Error Importing [sha3] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_sha3_mod))
 exit()
 
try:
 print('Attempting To Import [time] Module.')
 import time
except Exception as bad_time_mod:
 print('Error Importing [time] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_time_mod))
 exit()

try:
 print('Attempting To Import [string] Module.')
 import string
except Exception as bad_string_mod:
 print('Error Importing [string] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_string_mod))
 exit()

try:
 print('Attempting To Import [pickle] Module.')
 import pickle
 try_pickle = True
except Exception as bad_pickle_mod:
 print('Error Importing [pickle] Module. Instructing Program To Turn Off Pickle DB.')
 print('Error: '+str(bad_pickle_mod))
 try_pickle = False

try:
 print('From [bitcoin] Attempting To Import [sha256] Method.')
 from bitcoin import sha256 as sha
except Exception as bad_btcsha_mod:
 print('Error Importing [sha256] Method From [bitcoin] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_btcsha_mod))
 exit()

try:
 print('From [bitcoin] Attempting To Import [privtopub] Method.')
 from bitcoin import privtopub as public
except Exception as bad_privtopub_mod:
 print('Error Importing [privtopub] Method From [bitcoin] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_privtopub_mod))
 exit()

try:
 print('From [bitcoin] Attempting To Import [pubtoaddr] Method.')
 from bitcoin import pubtoaddr as addr
except Exception as bad_pubtoaddr_mod:
 print('Error Importing [pubtoaddr] Method From [bitcoin] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_pubtoaddr_mod))
 exit()

print('Imports Complete')
if try_pickle == True:
 print('Attempting To Unpickle BTC-DB.')
 try:
  bitcoin_highvalue_list = pickle.load(open('./btc-high-value.vnm','rb'))
  pickle_db = True
 except Exception as E:
  print('Need To Make New btc-high-value.p DB File Just A Moment')
  bitcoin_highvalue_list = []
  pickle.dump(bitcoin_highvalue_list, open('./btc-high-value.vnm','wb'))
  pickle_db = True

################ Objectt Section #############################################


class Flayer():
 def __init__(self):
  print('Setting Up Data and Live Connections Now')
  self.open_data_container()
  self.set_constant_storage()
  self.setup_menu()
  
 def open_data_container(self):
  global data_storage
  data_storage = dict()

 def set_constant_storage(self):
  global data_storage
  data_storage['file_num'] = 0
  data_storage['stop_point'] = 2500
  data_storage['start_time'] = time.localtime()
  data_storage['chars'] = dict()
  data_storage['record file'] = dict()
  data_storage['btc file'] = dict()
  data_storage['last int file'] = dict()
  data_storage['chars']['menu'] = dict()
  data_storage['chars']['menu']['item 1'] = list("0123456789")
  data_storage['chars']['menu']['item 1 size'] = len(data_storage['chars']['menu']['item 1'])
  data_storage['chars']['menu']['item 2'] = list("0123456789abcdef")
  data_storage['chars']['menu']['item 2 size'] = len(data_storage['chars']['menu']['item 2'])
  data_storage['chars']['menu']['item 3'] = list("!@#$%^&*()")
  data_storage['chars']['menu']['item 3 size'] = len(data_storage['chars']['menu']['item 3'])
  data_storage['chars']['menu']['item 4'] = list("0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#0123456789")[:66]
  data_storage['chars']['menu']['item 4 size'] = len(data_storage['chars']['menu']['item 4'])
  data_storage['chars']['menu']['item 5'] = list(string.printable)[:]
  data_storage['chars']['menu']['item 5 size'] = len(data_storage['chars']['menu']['item 5'])
  data_storage['constant_pointer'] = 0
  data_storage['clear_pointer'] = 0
  data_storage['mock_pass'] = 'SLKDJFL'
  data_storage['solved'] = False
  data_storage['digits'] = list()
  data_storage['length capacity'] = 14
  
 def setup_menu(self):
  global data_storage
  print('''
Welcome to the setup menu your options are limited but still available please choose from the following:
1: "0123456789"
2: "0123456789abcdef"
3: "!@#$%^&*()"
4: "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#0123456789"[:66]
5: "string.printable"[:]  <-- All English Keyboard Input Available Including Tabs / Unknown Input.
''')
  choice = input('Please Type (INT) Selection And Press Enter: ')
  if choice == '1':
   data_storage['chars']['current'] = data_storage['chars']['menu']['item 1']
   data_storage['chars']['base'] = len(data_storage['chars']['current'])
   data_storage['chars']['size'] = data_storage['chars']['menu']['item 1 size']
   starting_at = input('Please Choose (INT) To Start At: ')
   try:
    int_check = int(starting_at) + 1
    data_storage['constant_pointer'] = int(starting_at)
    self.start_crack()
   except Exception as NI:
    print('You Need To Start With An Integer Returning To Setup Menu')
    print(starting_at)
    print('Error: '+str(NI))
    self.setup_menu()
  elif choice == '2':
   data_storage['chars']['current'] = data_storage['chars']['menu']['item 2']
   data_storage['chars']['base'] = len(data_storage['chars']['current'])
   data_storage['chars']['size'] = data_storage['chars']['menu']['item 2 size']
   starting_at = input('Please Choose (INT) To Start At: ')
   try:
    int_check = int(starting_at) + 1
    data_storage['constant_pointer'] = int(starting_at)
    self.start_crack()
   except Exception as NI:
    print('You Need To Start With An Integer Returning To Setup Menu')
    print(starting_at)
    print('Error: '+str(NI))
    self.setup_menu()
  elif choice == '3':
   data_storage['chars']['current'] = data_storage['chars']['menu']['item 3']
   data_storage['chars']['base'] = len(data_storage['chars']['current'])
   data_storage['chars']['size'] = data_storage['chars']['menu']['item 3 size']
   starting_at = input('Please Choose (INT) To Start At: ')
   try:
    int_check = int(starting_at) + 1
    data_storage['constant_pointer'] = int(starting_at)
    self.start_crack()
   except Exception as NI:
    print('You Need To Start With An Integer Returning To Setup Menu')
    print(starting_at)
    print('Error: '+str(NI))
    self.setup_menu()
  elif choice == '4':
   data_storage['chars']['current'] = data_storage['chars']['menu']['item 4']
   data_storage['chars']['base'] = len(data_storage['chars']['current'])
   data_storage['chars']['size'] = data_storage['chars']['menu']['item 4 size']
   starting_at = input('Please Choose (INT) To Start At: ')
   try:
    int_check = int(starting_at) + 1
    data_storage['constant_pointer'] = int(starting_at)
    self.start_crack()
   except Exception as NI:
    print('You Need To Start With An Integer Returning To Setup Menu')
    print(starting_at)
    print('Error: '+str(NI))
    self.setup_menu()
  elif choice == '5':
   data_storage['chars']['current'] = data_storage['chars']['menu']['item 5']
   data_storage['chars']['base'] = len(data_storage['chars']['current'])
   data_storage['chars']['size'] = data_storage['chars']['menu']['item 5 size']
   starting_at = input('Please Choose (INT) To Start At: ')
   try:
    int_check = int(starting_at) + 1
    data_storage['constant_pointer'] = int(starting_at)
    self.start_crack()
   except Exception as NI:
    print('You Need To Start With An Integer Returning To Setup Menu')
    print(starting_at)
    print('Error: '+str(NI))
    self.setup_menu()
  
 def check_password(self):
  if data_storage['mock_pass'] == '':
   print('Your password is empty')
   data_storage['solved'] = True
  elif data_storage['mock_pass'] == data_storage['chars']['current'][data_storage['constant_pointer']]:
   print('Your password is ' + str(data_storage['chars']['current'][data_storage['constant_pointer']]))
   data_storage['solved'] = True
  else:
   data_storage['constant_pointer'] += 1
 
 
 def numberToBase(self, cont_pointer, char_base):
  global data_storage
  data_storage['digits'] = []
  while cont_pointer:
    data_storage['digits'].append(int(cont_pointer % char_base))
    cont_pointer /= char_base
  return data_storage['digits'][::-1]


 def clear_screen(self):
  global data_storage
  os.system('cls')
  data_storage['clear_pointer'] = 0

 def hash_calculations(self,word_used, word_size):
  global data_storage
  global First_Display_Targets
  word = word_used
  data_storage['hashed'] = sha(str(word[-word_size:]))
  btc_priv = data_storage['hashed']
  pub = public(btc_priv)
  address = addr(pub)
  data_storage['constant_pointer'] += 1
  data_storage['clear_pointer'] += 1
  if First_Display_Targets == False:
   print('Displaying List Of Targets We Are Checking Against.')
   print(bitcoin_highvalue_list)
   First_Display_Targets = True
  if address in bitcoin_highvalue_list:
   print('Found Bitcoin High Value Address.')
   print('Found history on address: {}'.format(address)+'\n')
   print('Private: {}'.format(btc_priv)+'\n')
   print('Word: {}'.format(str(word[-word_size:]))+'\n')
   pickle.dump(btc_priv,open('{}.vnm'.format(address),'wb'))
   print('We Are Paused')
   paused = input('>>: ')
  elif address not in bitcoin_highvalue_list:
   print('Last Int: {}'.format(data_storage['constant_pointer']))
   print('Word: {}'.format(str(word[-word_size:])))

 def start_crack(self):
  try:
   if not data_storage['solved']:
     while int(data_storage['constant_pointer']) < (int(data_storage['chars']['base']) ** int(data_storage['length capacity'])) - int(data_storage['constant_pointer']):
      lst = self.numberToBase(data_storage['constant_pointer'], data_storage['chars']['base'])
      word = ''
      for x in lst:
       word += str(data_storage['chars']['current'][x])
      if data_storage['clear_pointer'] >= data_storage['stop_point']:
       self.clear_screen()
      if data_storage['constant_pointer'] >= 0 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 1:
       self.hash_calculations(word, 1)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 1 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 2:
       self.hash_calculations(word, 2)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 2 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 3:
       self.hash_calculations(word, 3)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 3 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 4:
       self.hash_calculations(word, 4)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 4 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 5:
       self.hash_calculations(word, 5)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 5 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 6:
       self.hash_calculations(word, 6)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 6 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 7:
       self.hash_calculations(word, 7)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 7 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 8:
       self.hash_calculations(word, 8)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 8 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 9:
       self.hash_calculations(word, 9)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 9 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 10:
       self.hash_calculations(word, 10)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 10 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 11:
       self.hash_calculations(word, 11)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 11 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 12:
       self.hash_calculations(word, 12)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 12 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 13:
       self.hash_calculations(word, 13)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 13 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 14:
       self.hash_calculations(word, 14)
      else:
       print('All Accounts Cracked.')
       exit()
  except KeyboardInterrupt as KI:
   try:
    print('Welcome To The Pause Section. PRESS CTRL+C AGAIN TO EXIT.')
    paused = input('Press Enter Or Input Extra Options To Continue. >>: ')
    if paused.lower() == '':
     self.start_crack()
    elif paused.lower() == 'help':
     print('You Need A Lot More Then Help')
     self.start_crack()
   except KeyboardInterrupt as KI2:
    print('Instructing Program To Exit.')
    exit()

print('Starting Flayer Program You May Press CTRL+C At Any Time To Enter Pause Section. Happy Flaying!')
flay = Flayer()
