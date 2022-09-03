import random
import time
# import keyboard
import subprocess

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.keys import Keys


s = Service(r'D:\Drivers\msedgedriver.exe')
driver = webdriver.Edge(service=s)
driver.set_page_load_timeout(15)

file_path = r"D:\Ideas\Funny steam names.txt"


# driver.get('https://randomnamegenerators.com/fantasy-name-generators/warrior-name-generator/?v=1')
#
# wait = WebDriverWait(driver, 15)
# wait.until(expected_conditions.title_contains("Warrior"))
#
# print("Entering: " + driver.title)
#
# Randomname = driver.find_element(By.CLASS_NAME, "full")  # bruh I'm a genius.
#
# print("Awaiting name to load...")
#
# while Randomname.text.__contains__("Loading"):
#     time.sleep(2)
#     Randomname = driver.find_element(By.CLASS_NAME, "full")  # retrying until name loads.
#
# print("Name successfully loaded!")
# name = Randomname.text
#
# print("Acquired name: " + name + " Successfully!")

# driver.close()
# driver = webdriver.Edge(service=s)  # starting a new session to avoid exceptions and errors


def signin():
    finished = 0
    while finished == 0:
        try:
            driver.get('https://steamcommunity.com/id/gbucks/')  # will time out in 15 secs if not loaded properly
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

    input_field1 = driver.find_element(By.XPATH, "//input[@type='text']")  # steam fucking sucks
    input_field1.send_keys("picwick2")

    time.sleep(1)

    input_field1 = driver.find_element(By.XPATH, "//input[@type='password']")
    input_field1.send_keys("Goomer1805")

    time.sleep(1)

    input_field1.submit()

    print("awaiting authenticator password (1 min duration)...")

    # executing index.js in steam guard grabber to generate the newest steam guard code
    p = subprocess.Popen(["powershell.exe", "./test.ps1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(out, err)

    f = open("D:/Downloads/steam-guard-grabber-main/steamauthcode.txt", "r")
    steamauthcode = f.read()
    # waiting until the new code is usable (gives next code instead of current code all the time)
    print("waiting 30 secs for code to be usable...")
    time.sleep(30)
    print("Read:" + steamauthcode)
    # inputting the code
    input_field1 = driver.find_element(By.XPATH, "//input[@type='text']")
    input_field1.send_keys(steamauthcode)

    wait1 = WebDriverWait(driver, 60)  # giving you 1 minute to enter the steam authenticator password correctly.
    wait1.until(expected_conditions.title_contains("Steam Community"))

    print("logged in successfully!")

    print("Entering: " + driver.title)

    time.sleep(1)  # giving you one second to regret the Edit profile and while true loop procedure


signin()

deathcount = 0
name1 = ""
currentT = time.time()
while True:

    # Generate random name from list:
    file = open(file_path)  # opening the file again every time so that I will be able to dynamically update it
    text = file.read()
    numoflines = 0  # recalculating the number of lines
    count = 0
    while count < len(text):
        if text[count] == ";":
            numoflines += 1
        count += 1

    i = random.randint(1, numoflines)  # symbolizes the number of lines in the text
    count = 0
    while i > 0 and count < len(text):
        if text[count] == ";":
            i -= 1
        count += 1
    count += 1  # skips over a " " (speculation)
    while text[count] != ";":
        name1 += text[count]
        count += 1

    print("Acquired name: " + name1)

    # Edit the steam profile:
    link = driver.find_element(By.LINK_TEXT, "Edit Profile")
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
        driver.get('https://steamcommunity.com/id/gbucks/')

    print("Entering: " + driver.title)

    print("operation commenced successfully!")
    print(time.time())
    # waits until an input from the keyboard was entered
    print("Generating new name again in 1 hr")
    name1 = ""
    time.sleep(3600)  # sleep for 1 hr
    # end of loop ---------------------------------------------------------------

# Take random picture for each name can be from search results of name on Google or random image from pictures folder
