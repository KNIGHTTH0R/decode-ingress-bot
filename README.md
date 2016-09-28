# decode-ingress-bot

- Install python3 and virtualenv
- Setup a python3 virtualenv and activate it:
```
$ virtualenv -p <path/to/python3> py3env
$ source py3env/bin/activate
(py3env)$ ...
```
- Install requirements using pip
```
(py3env)$ pip install -r requirements.txt
```
- Create a `secrets.py` file and add a `TG_BOT_TOKEN` variable to store your Telegram Bot token as obtained by @BotFather
- Launch your bot by running
```
(py3env)$ python bot.py
```

**Note: currently the bot supports only poll mode**
