import schedule
import time

from tronapi import Tron
from pprint import pprint

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'

# Define where to send
mainAccount = "TKSXDA8HfE9E1y39RczVQ1ZascUEtaSToF"
# Define where to check
accounts = dict([
    ("YOURADDRESSHERE","YOURPRIVATEKEYHERE"),
    ("YOURADDRESSHERE","YOURPRIVATEKEYHERE"),
    ("YOURADDRESSHERE","YOURPRIVATEKEYHERE"),
    ("YOURADDRESSHERE","YOURPRIVATEKEYHERE"),
])
# Define minmum amount to transfer
min_withdraw = 1
scanMin = 60


tron = Tron(full_node=full_node,
        solidity_node=solidity_node,
        event_server=event_server)


def setTronPK(pk):
    tron.private_key = pk
    tron.default_address = tron.address.from_private_key(pk).base58



def job():
    for address in accounts:
        print("Checking " + address)
        balance = tron.fromSun(tron.trx.get_balance(address))
        if balance>=min_withdraw:
            setTronPK(accounts[address])
            # Send
            print("Sending {} TRX to {}".format(balance, mainAccount))
            try:
                tron.trx.send(mainAccount, float(balance))
            except:
                print("Error while transfering, please try again...")
            

print("Initiating TRX divided gathering...")
# add job schedule
print("Scheduling job...")
#schedule.every(1).minutes.do(job)
schedule.every(scanMin).seconds.do(job)

# just wait 
while 1:
    schedule.run_pending()
    time.sleep(60)
