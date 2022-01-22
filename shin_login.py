import configparser
import datetime
import win32gui
import win32con
import getpass
import time
import os
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium import webdriver

# Open the website and fill the credentials at a given time
def autolog():

    while True:
        if (
            datetime.datetime.now().hour == hour
            and datetime.datetime.now().minute == minute
        ):

            # Open designated browser
            try:
                if browser == "Chrome":
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                elif browser == "Firefox":
                    driver = webdriver.Firefox(
                        executable_path=GeckoDriverManager().install()
                    )
                elif browser == "Opera":
                    driver = webdriver.Opera(OperaDriverManager().install())
                elif browser == "Edge":
                    driver = webdriver.Edge(egde_driver_path)

                driver.maximize_window()
                driver.get(
                    "https://webstatic-sea.mihoyo.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&mhy_auth_required=true&mhy_presentation_style=fullscreen&utm_source=tools&lang=en-us&bbs_theme=dark&bbs_theme_device=1"
                )

                driver.find_element_by_class_name("mhy-hoyolab-account-block").click()
                driver.find_element_by_css_selector(
                    "input[type='text'][placeholder='Username/Email']"
                ).send_keys(login)
                driver.find_element_by_css_selector(
                    "input[type='password'][placeholder='Password']"
                ).send_keys(password)

                # Press the login button
                if submit == True:
                    driver.find_element_by_class_name("mhy-login-button").click()

                # Prevent the browser from closing
                while True:
                    try:
                        driver.find_element_by_class_name("mhy-hoyolab-account-block")

                    except:
                        break

                    time.sleep(1)
                break

            except:
                pass

        time.sleep(1)


# Add to Windows startup folder via .bat file
def startup(file_path=""):

    try:
        open(
            r"C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
            % getpass.getuser()
            + "\\"
            + "open.bat",
            "r",
        )
    except FileNotFoundError:
        bat_file = open(
            r"C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
            % getpass.getuser()
            + "\\"
            + "open.bat",
            "w+",
        )
        bat_file.write(r'start "" "%s"' % file_path)


if __name__ == "__main__":

    configuration = configparser.ConfigParser()

    # Read the config file with settings
    try:
        configuration.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        configuration.options("Configuration")
        login = configuration.get("Configuration", "login")
        password = configuration.get("Configuration", "password")
        browser = configuration.get("Configuration", "browser")
        hour = configuration.getint("Configuration", "hour")
        minute = configuration.getint("Configuration", "minute")
        file_path = configuration.get("Configuration", "file_path")
        egde_driver_path = configuration.get("Configuration", "edge_path")
        submit = configuration.getboolean("Configuration", "submit")
        hide_window = configuration.getboolean("Configuration", "hide_window")

    except FileNotFoundError:
        pass

    startup(file_path=file_path)

    # Hiding console window
    if hide_window == True:
        win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

    autolog()
