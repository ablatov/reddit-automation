# Reddit automation
This is a small project of test automation for some functionality of https://reddit.com

# Environment setup
1. Install Python version >=3.8 and all dependencies via maven.
2. Setup account on MailSlurp (dummy emails).
3. Register client on Reddit with email from previous step.
4. Get client_id and client_secret after creating a script app [here](https://www.reddit.com/prefs/apps) and 
put them with other data to bot1 section in [praw.ini](praw.ini) file.
5. Clone repo and install requirements:
```
pip install -r requirements.txt
```

# Tests running
In terminal from project path execute:
```
python -m pytest -v tests\
```

# Other documentation
PRAW library - https://praw.readthedocs.io/en/stable/

Pytest docs - https://docs.pytest.org/en/7.1.x/
