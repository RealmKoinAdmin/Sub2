import bitcoin
import pickle
setUp = False
data = pickle.load(open('btc-high-value.vnm','rb'))
starting = 1
def set_up():
 global Input
 global setUp
 print('Would You Like Auto Or Manual?')
 Question = input('>>: ')
 if Question.lower() == 'auto':
  try:
   Number = pickle.load(open('NumberFlayerMulti-Number.vnm','rb'))
  except Exception as No_Number_File:
   print('Need New Auto File')
   print('What Number Are We Starting With?')
   Number = input('>>: ')
   try:
    print('New Auto File Created')
    pickle.dump(int(Number),open('NumberFlayerMulti-Number.vnm','wb'))
   except Exception as Bad_Pickle:
    print('Something Fucky With Auto File Creation: [{}].'.format(Bad_Pickle))
 elif Question.lower() == 'manual':
  print('Need New Auto File')
  print('What Number Are We Starting With?')
  Number = input('>>: ')
 try:
  Input = int(Number)
  setUp = True
 except Exception as Not_A_Fucking_Number:
  print('Not A Fucking Number Try Again')

def cycle(number):
 global starting
 starting = 1
 ending = 65
 while starting < ending:
  bitcoined = dict()
  bitcoined['hash_0'] = bitcoin.sha256(str(number)*starting)
  bitcoined['hash_1'] = bitcoin.sha256(hex(number)*starting)
  bitcoined['hash_2'] = bitcoin.sha256(hex(number)[2:]*starting)
  bitcoined['pub_0'] = bitcoin.privtopub(bitcoined['hash_0'])
  bitcoined['pub_1'] = bitcoin.privtopub(bitcoined['hash_1'])
  bitcoined['pub_2'] = bitcoin.privtopub(bitcoined['hash_2'])
  bitcoined['addr_0'] = bitcoin.pubtoaddr(bitcoined['pub_0'])
  bitcoined['addr_1'] = bitcoin.pubtoaddr(bitcoined['pub_1'])
  bitcoined['addr_2'] = bitcoin.pubtoaddr(bitcoined['pub_2'])
  print('Running Cycle: [{}*{}]/[{}*{}]/[{}*{}] | Break Attempts: [{}].'.format(Input,starting,hex(Input),starting,hex(Input)[2:],starting,
                                                                                (len(data)*((Input*64)*3))/1e8))
  if len(str(number)*starting) == 64:
   try:
    keyed_number = dict()
    keyed_number['hash_number'] = str(number)*starting
    keyed_number['pub_number'] = bitcoin.privtopub(keyed_number['hash_number'])
    keyed_number['addr_number'] = bitcoin.pubtoaddr(keyed_number['pub_number'])
    print('Checking [{}]'.format(keyed_number['addr_number']))
   except Exception as Number_E:
    print('Raw Number Error: [{}].'.format(str(Number_E)))
    keyed_number = dict()
    keyed_number['addr_number'] = ''
  elif len(str(number)*starting) != 64:
   keyed_number = dict()
   keyed_number['addr_number'] = ''
  if len((hex(number)[2:]*starting)) == 64:
   try:
    keyed_hex = dict()
    keyed_hex['hash_hex'] = hex(number)[2:]*starting
    keyed_hex['pub_hex'] = bitcoin.privtopub(keyed_hex['hash_hex'])
    keyed_hex['addr_hex'] = bitcoin.pubtoaddr(keyed_hex['pub_hex'])
    print('Checking [{}]'.format(keyed_hex['addr_hex']))
   except Exception as Hex_E:
    print('Raw Hex Error: [{}]'.format(Hex_E))
    keyed_hex = dict()
    keyed_hex['addr_hex'] = ''
  elif len((hex(number)[2:]*starting)) != 64:
   keyed_hex = dict()
   keyed_hex['addr_hex'] = ''
  if bitcoined['addr_0'] in data:
   print('Found One! Address: {0} | PrivateKey: {1} | Hashed: {2}'.format(bitcoined['addr_0'],bitcoined['hash_0'],number))
   pickle.dump(bitcoined,open('{}-Found.vnm'.format(bitcoined['addr_0']),'wb'))
   print('{}-Found.vnm Created!'.format(bitcoined['addr_0']))
   print('We Are Paused!')
   Paused = input('>>: ')
  if bitcoined['addr_1'] in data:
   print('Found One! Address: {0} | PrivateKey: {1} | Hashed: {2}'.format(bitcoined['addr_1'],bitcoined['hash_1'],hex(number)))
   pickle.dump(bitcoined,open('{}-Found.vnm'.format(bitcoined['addr_1']),'wb'))
   print('{}-Found.vnm Created!'.format(bitcoined['addr_1']))
   print('We Are Paused!')
   Paused = input('>>: ')
  if bitcoined['addr_2'] in data:
   print('Found One! Address: {0} | PrivateKey: {1} | Hashed: {2}'.format(bitcoined['addr_2'],bitcoined['hash_2'],hex(number)[2:]))
   pickle.dump(bitcoined,open('{}-Found.vnm'.format(bitcoined['addr_2']),'wb'))
   print('{}-Found.vnm Created!'.format(bitcoined['addr_2']))
   print('We Are Paused!')
   Paused = input('>>: ')
  if keyed_number['addr_number'] in data:
   print('Found One! Address: {0} | PrivateKey: {1} | Hashed: {2}'.format(keyed_number['addr_number'],keyed_number['hash_number'],'NONE/RAW'))
   pickle.dump(bitcoined,open('{}-Found.vnm'.format(keyed_number['addr_number']),'wb'))
   print('{}-Found.vnm Created!'.format(keyed_number['addr_number']))
   print('We Are Paused!')
   Paused = input('>>: ')
  if keyed_hex['addr_hex'] in data:
   print('Found One! Address: {0} | PrivateKey: {1} | Hashed: {2}'.format(keyed_hex['addr_hex'],keyed_hex['hash_hex'],'NONE/RAW'))
   pickle.dump(bitcoined,open('{}-Found.vnm'.format(keyed_hex['addr_hex']),'wb'))
   print('{}-Found.vnm Created!'.format(keyed_hex['addr_hex']))
   print('We Are Paused!')
   Paused = input('>>: ')
  starting += 1
while True:
 if setUp != True:
  set_up()
 #print('Running Cycle: [{}*{}]/[{}*{}]/[{}*{}] | Break Attempts: [{}].'.format(Input,starting,hex(Input),starting,hex(Input)[2:],
  #                                                                             starting,(len(data)*(Input*3))/1e8))
 cycle(Input)
 pickle.dump(Input,open('NumberFlayerMulti-Number.vnm','wb'))
 Input += 1
