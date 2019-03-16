# tron-python-automate-send
Python tool automate send TRX from dividend accounts to main wallet

### Config

- Set main destination with ```mainAccount="ADDRESS"```
- Set lookup accounts with  ```accounts = dict([
    ("YOURADDRESSHERE","YOURPRIVATEKEYHERE"),...])```
- Set min withdraw with ```min_withdraw = X``` TRX amount
- Set scan timer with ```scanMin = 60``` MIN

### Dependencies
> pip install -r requirements.txt

### RUN
> python main.py