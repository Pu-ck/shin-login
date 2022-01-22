# shin-login
Automate Genshin Impact Daily Check-In

Simple Python script for Windows to automate and remind receiving Genshin Impact Daily Rewards. Creates the .bat file in startup folder in order to run itself in background and automatically open the chosen browser everyday at designated time, filling in the credentials - the CAPTCHA must be resolved manually. Config.ini content:
- login
- password
- browser: Chrome, Firefox, Opera or Edge (requires manually downloaded webdriver)
- hour
- minute
- file_path: location of the script itself
- edge_path: location of the Edge webdriver
- submit: True/False, press the login button automatically
- hide_window: True/False, hiding the console window

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
