# Selenium Steam Account Logger and Name Alternator
- A steam webscraper done using selenium and the msedge webdriver. 
- It's purpose is to log into your steam account and change your steam profile name every hour automatically.
- It could also be used for other purposes but that would require you to alter the code in main.py.
# Requirements For Usage
### 1. You MUST have NODE.JS installed on your machine.
- You can install Node.js [here](https://nodejs.org/en/download/).
### 2. You MUST use a machine with a WINDOWS OS in order for the Powershell script to work.
- Otherwise, you must change the powershell script into your OS's equivalent.
### 3. You MUST have an Edge webdriver and an Edge Browser installed on your machine.
- If you prefer a different browser, you must alter the code in main.py for it to work).
- You can get the webdriver [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
### 4. You MUST have a Steam Authenticator Application installed on a Rooted Machine (Rooted = has a file explorer).
- You can get the steam desktop authenticator application [here](https://github.com/jessecar96/steamdesktopauthenticator).
### 5. You should use an IDE such as Pycharm or Visual Studio Code for execution of this project.
- I think that in other IDEs it might get more complicated
# What You Need To Know Before Using This Script
### 1. main.py
- The main script, it is the script that does the whole process of signing in to steam and changing your name.
- You will have to insert a lot of information in the signin function and outside of  it, therefore you MUST edit it.
### 2. test.ps1
- A powershell script that is in charge of executing the index.js file inside the steam guard grabber folder
- A path for the index.js file's location MUST be given within it's code.
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
### Felipe Almeida (@fgalmeida) for the steam-auth-grabber project.
- I altered his index.js code a tad by making it also write the steam authenticator code into the steamauthcode.txt text file.
- You can find his untouched steam-guard-grabber project [here](https://github.com/fgalmeida/steam-guard-grabber).

# License
### I allow usage of my contributed part in this project for any usage excluding:
- Usage for False purposes such as hacking.
- Usage for the purpose of profiting.
### As for Felipe Almeida (@fgalmeida) who wrote the steam-auth-grabber part of the project:
- Read his license which is located [here](https://github.com/fgalmeida/steam-guard-grabber/blob/main/LICENSE).
