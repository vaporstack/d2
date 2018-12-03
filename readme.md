# d2


## setup

```
#	a hastily constructed supybot replacement that is in no way
#	as capable of supybot

#	install

# clone and cd obv

virtualenv -p python3 .

source bin/activate

pip install discord.py

cp credentials.example.json credentials.json

#	obviously put your key into credentials file

python runner.py
```
