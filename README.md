# Selenium Steam Logger and Name Changer
Steam webscraper, will log into steam and change your name every hour automatically.
# Requirements for usage:
### 1. You MUST have NODE.JS installed on your machine.
### 2. You MUST use a machine with a WINDOWS OS in order for the Powershell script to work, otherwise you must change the powershell script into your OS's alternative.
# What You Need To Know Before Usage
### 1. main.py
- The main script, it is the script that does the whole process of signing in to steam and chaning your name.
- You will have to insert a lot of information in the signin function and outside it, therefore you MUST edit it.
### 2. test.ps1
- A powershell script that is in charge of executing the index.js file inside the steam guard grabber folder
### 3. index.js
- Is located inside of the steam-guard-grabber folder
- Requires your steam username password and sharedsecrets which it gets through the config.json file
- Will Interact with steam and grab your steam authenticator code in order for main.py to log into your account.
### 4. config.json
- Is located inside of the steam-guard-grabber folder
- You MUST insert in there your steam account username, password and "shared secrets"
- You can get your "shared secrets" by installing a steam guard authenticator on your Desktop or on a Rooted Phone.
- then go into the maFiles folder and the .maFile file, in there you will find the "shared secrets" code.
### 5. steamauthcode.txt
- DO NOT ALTER IT'S NAME WITHOUT CHANGING IT IN THE CODE TOO (usages: main.py, index.js).
- DO NOT CHANGE IT'S CONTENTS DURING RUN TIME.
- it will always contain your steam authentication code which main.py needs to use in order to log into your account.
### 6. SteamNames.txt
- DO NOT ALTER IT'S NAME WITHOUT CHANGING IT IN THE CODE TOO (usages: main.py).
- A file containing your own custom names for the random generator in main.py to pick from.
- YOU MUST SEPERATE EACH NAME WITH A ";" SIGN.
# Credits
### Felipe Almeida (@fgalmeida) for the steam-auth-grabber project. you can find it [here](https://github.com/fgalmeida/steam-guard-grabber).

# License
### I allow usage of my contributed part in this project for any usage excluding:
- Usage for False purposes such as hacking
- Usage for the purpose of profiting.

