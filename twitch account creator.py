import selenium
from selenium import webdriver

import time
import string
import random


def randomStringDigits(stringLength=13) :
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def codemain():
    providers = ["@gmail.com", "@googlemail.com", "@gmx.de","@outlook.com","@outlook.fr","@yandex.ru","@mail.com","@yahoo.co.uk","@protonmail.ch"]


    rngusername = randomStringDigits(13)
    rngpassword = randomStringDigits(15)
    rngemail = randomStringDigits(10)
    fullemail = (rngemail) + random.choice(providers)


    URL = 'https://www.twitch.tv/signup'
    DRIVER = webdriver.Chrome("chromedriver.exe")


    DRIVER.get(URL)
    time.sleep(1.4)
    usrnamebox = DRIVER.find_element_by_id('signup-username')
    usrnamebox.send_keys(rngusername)
    passbox = DRIVER.find_element_by_id('password-input')
    passbox.send_keys(rngpassword)
    passconfbox = DRIVER.find_element_by_id('password-input-confirmation')
    passconfbox.send_keys(rngpassword)
    # we need to do a birthday month select thing
    monthbox = DRIVER.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/select')
    monthbox.send_keys('january')
    daybox = DRIVER.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/div/input')
    daybox.send_keys(random.randrange(1, 30))
    yearbox = DRIVER.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input')
    yearbox.send_keys(random.randrange(1970, 2002))
    emailbox = DRIVER.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[4]/div/div[2]/input')
    emailbox.send_keys(fullemail)
    time.sleep(1.5)
    signup = DRIVER.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[5]/button')
    signup.click()
    captchadone = input('Please complete the captcha. Type anything once it is complete.')
    if captchadone == captchadone:
        time.sleep(3)
        remindmelater = DRIVER.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[3]/div[2]/div/button')
        remindmelater.click()
        with open('userpass.txt', 'a') as f :
            f.write(rngusername + ':' + rngpassword + '\n')
        with open('emailuserpass.txt', 'a') as f :
            f.write(fullemail + ':' + rngusername + ':' + rngpassword + '\n')
        DRIVER.quit()

        restart = input('Do you want to restart the script? y/n')
        if restart == 'y':
            codemain()

codemain()


