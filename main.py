import random
import time
import subprocess

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.service import Service

# using a driver of the Edge browser because the Google one is not upto date
s = Service(r'D:\YourDriverFolder\msedgedriver.exe')
driver = webdriver.Edge(service=s)
driver.set_page_load_timeout(15)

# location of your txt file containing the names you want
# if the location is not under the same folder as the rest of the project then you will have to insert your path
file_path = r"SteamNames.txt"


# signin funtion, you will have to insert a lot of information here so DO NOT IGNORE -----------------------------------
def signin():
    finished = 0
    while finished == 0:
        try:
            driver.get('https://steamcommunity.com/id/yoursteamid/')  # logs into your steam profile (fill this id in)
            if driver.title.__contains__("Steam"):
                finished = 1
            else:
                print("retrying...")
        except TimeoutException as exception:
            print(exception)
            print("TIMED OUT, retrying...")
            time.sleep(5)

    print("Entering: " + driver.title)

    link1 = driver.find_element(By.LINK_TEXT, "login")
    link1.click()

    wait1 = WebDriverWait(driver, 15)
    wait1.until(expected_conditions.title_contains("Sign"))

    print("Entering: " + driver.title)
    print("logging in...")

    time.sleep(1)

    # inserting username and password details
    input_field1 = driver.find_element(By.XPATH, "//input[@type='text']")
    input_field1.send_keys("username")  # insert your username here

    time.sleep(1)

    input_field1 = driver.find_element(By.XPATH, "//input[@type='password']")
    input_field1.send_keys("password")  # insert your password here

    time.sleep(1)

    input_field1.submit()

    print("awaiting authenticator password (1 min duration)...")

    # executing index.js in steam guard grabber to generate the newest steam guard code
    # in order for this to work you must follow these steps:
    # you will have to insert in the config file of the steam guard grabber your username, password and shared secrets
    # to get the shared secrets you must have a steam authenticator on your desktop or a rooted phone.
    # go to the .maFiles folder and open the .maFile in a text editor.
    # you will find in there your shared secrets.
    p = subprocess.Popen(["powershell.exe", "./test.ps1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # executing index.js with a powershell command.
    out, err = p.communicate()
    print(out, err)  # error logger

    # the code has now been written into a steamauthcode txt saver of your choice.
    # now we must grab it and get the code in order to insert it to the steam authenticator.
    f = open("steam-guard-grabber-main/steamauthcode.txt", "r")
    steamauthcode = f.read()
    # waiting until the new code is usable (steam auth grabber gives next code instead of current code all the time)
    print("waiting 30 secs for code to be usable...")
    time.sleep(30)
    print("Read:" + steamauthcode)
    # inputting the code
    input_field1 = driver.find_element(By.XPATH, "//input[@type='text']")
    input_field1.send_keys(steamauthcode)

    wait1 = WebDriverWait(driver, 60)  # 1 minute wait until timeout, should load by then.
    wait1.until(expected_conditions.title_contains("Steam Community"))

    print("logged in successfully!")

    print("Entering: " + driver.title)

    time.sleep(1)  # giving you one second to regret the Edit profile and while true loop procedure
# signin function over -------------------------------------------------------------------------------------------------


signin()  # calling the function in order to sign in to steam.

name1 = ""  # will recieve the randomly generated name later.

# while true loop begins -----------------------------------------------------------------------------------------------
while True:
    # Generate random name from list:
    file = open(file_path)  # opening the file again every time so that I will be able to dynamically update it
    text = file.read()
    numoflines = 0  # recalculating the number of lines
    count = 0
    # you must put a ";" after every name you put in the text file or else it won't work
    while count < len(text):
        if text[count] == ";":
            numoflines += 1
        count += 1

    i = random.randint(1, numoflines)  # symbolizes the number of lines in the text
    count = 0
    while i > 1 and count < len(text):
        if text[count] == ";":
            i -= 1
        count += 1
    # count is currently located at the first letter of the chosen word
    while text[count] != ";":
        name1 += text[count]
        count += 1

    print("Acquired name: " + name1)

    # Edit the steam profile:
    link = driver.find_element(By.LINK_TEXT, "Edit Profile")
    # checking if there is a need to sign in again or not.
    if link is not None:
        link.click()
        try:
            wait = WebDriverWait(driver, 15)
            wait.until(expected_conditions.title_contains("Edit Profile"))
        except TimeoutException as e:
            url = driver.current_url
            driver.get(url)
    else:
        signin()

    print("Entering: " + driver.title)

    input_field = driver.find_element(By.NAME, "personaName")

    time.sleep(1)  # giving you one second to regret naming yourself something different
    while input_field is None:
        input_field = driver.find_element(By.NAME, "personaName")
    driver.implicitly_wait(10)
    input_field.clear()
    time.sleep(1)  # for cool effect
    input_field.send_keys(name1)

    time.sleep(1)  # cooldown

    input_field.submit()

    print("Submmition was successful, heading back to profile page...")

    time.sleep(1)

    link = driver.find_element(By.LINK_TEXT, "Back to Your Profile")
    link.click()

    try:
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.title_contains("Steam Community"))
    except TimeoutException:
        # goes back to your profile page, insert your profile page id here again.
        driver.get('https://steamcommunity.com/id/yoursteamid/')

    print("Entering: " + driver.title)

    print("operation commenced successfully!")
    print(time.time())
    # waits until an input from the keyboard was entered
    print("Generating new name again in 1 hr")
    name1 = ""  # clearing name.
    time.sleep(3600)  # waits for 1 hr
# end of loop ----------------------------------------------------------------------------------------------------------
