print(''' Welcome To Bitcoin Seed Eater Please Be Patient While I Import The Following Modules And Packages.''')
################ Import Section #############################################
try:
 print('Attempting To Import [os] Module.')
 import os
except Exception as bad_os_mod:
 print('Error Importing [os] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_os_mod))
 exit()
 
try:
 print('Attempting To Import [time] Module.')
 import time
except Exception as bad_time_mod:
 print('Error Importing [time] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_time_mod))
 exit()
import bitcoin

try:
 print('Attempting To Import [pickle] Module.')
 import pickle
except Exception as bad_pickle_mod:
 print('Error Importing [pickle] Module. Instructing Program To Turn Off Pickle DB.')
 print('Error: '+str(bad_pickle_mod))
try:
 btc_data = pickle.load(open('btc-high-value.vnm','rb'))
except Exception as Bad_Database:
 print(Bad_Database)

try:
 Seed_Db = pickle.load(open('SingleSeed-Flayer.vnm', 'rb'))
except Exception as Need_File:
 Seed_Db = dict()
 Seed_Db['forward'] = 0
 pickle.dump(Seed_Db,open('SingleSeed-Flayer.vnm', 'wb'))


################ Objectt Section #############################################

class SeedFlaying():
 def __init__(self,init_starting_0):
  self.extract_privatekey(init_starting_0)

 def extract_privatekey(self,starting_0):
  global forward_to_send_0
  global forward_to_send_1
  Sending = list()
  forward = hex(starting_0)
  if len(forward[2:]) < 64:
   forward_pad = '0'*(64-len(forward[2:]))
   forward_to_send_0 = forward_pad+forward[2:]
   forward_to_send_1 = forward[2:][::-1]+forward_pad
   Sending.append(forward_to_send_0)
   Sending.append(forward_to_send_1)
   Sending.append(bitcoin.sha256(forward_to_send_0))
   Sending.append(bitcoin.sha256(forward_to_send_1))
   self.btc_center(Sending)
  if int(len(forward[2:])) == int(64):
   forward_to_send_0 = forward[2:]
   forward_to_send_1 = forward[2:][::-1]
   Sending.append(forward_to_send_0)
   Sending.append(forward_to_send_1)
   Sending.append(bitcoin.sha256(forward_to_send_0))
   Sending.append(bitcoin.sha256(forward_to_send_1))
   self.btc_center(Sending)
  if int(len(forward[2:])) > int(64):
   print('Forward Seeds Are Done.')

 def btc_center(self, privateKeys):
  ADDY = list()
  KEYS = dict()
  for PK in privateKeys:
   pub = bitcoin.privtopub(PK)
   address = bitcoin.pubtoaddr(pub)
   ADDY.append(address)
   NEW = {address: PK}
   KEYS.update(NEW)
  print('Checking Addresses: [{}]'.format(ADDY))
  self.check_address(ADDY,KEYS)

 def check_address(self,address_to,pk):
  for A in address_to:
   if A in btc_data:
    print('We Found An Address!')
    print('Address: [{}] Privatekey: [{}]'.format(A,pk[A]))
    found = dict()
    found['Address'] = A
    found['Private'] = pk[A]
    pickle.dump(found,(open('{}-Found.vnm'.format(A), 'wb')))
    print('We Are Paused')
    Paused = input('>>: ')
     
    




FlaySeeds = True
Amount = 250000
Ticker = 0
Clear = 0
while FlaySeeds:
 
 if Clear >= 200:
  os.system('cls')
  Clear = 0
 if Ticker <= Amount:
   Seed_Db = pickle.load(open('SingleSeed-Flayer.vnm', 'rb'))
   SeedFlayer = SeedFlaying(Seed_Db['forward'])
   Seed_Db['forward'] += 1
   Ticker += 1
   Clear += 1
   print('Ticker Count [{}]/[{}] Left.'.format(Ticker,Amount-Ticker))
   pickle.dump(Seed_Db,open('SingleSeed-Flayer.vnm', 'wb'))
 elif Ticker > Amount:
   print('Finished With [{}] Seeds.'.format(Amount))
   FlaySeeds = False
exit()
