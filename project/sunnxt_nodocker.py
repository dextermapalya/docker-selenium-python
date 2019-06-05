import time
import unittest
import os
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains, keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from signin_parameters import * #all test page parameters are declared in this file
from site_parameters import * #all site parameters are declared in this file
from log_setup import get_logger

delay = 15 #5 seconds delay to find any element

class SunNxtHomepage(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Chrome( chrome_driver_path )
        address = os.getenv('NODE_HUB_ADDRESS', '192.168.112.2')
        grid = 'http://{0}:4444/wd/hub'.format(address)
        #self.browser = webdriver.Remote(
        #    command_executor=f'http://{address}:4444/wd/hub',
        #    desired_capabilities=caps
        #)

        #self.browser = webdriver.Remote(
        #                    command_executor = 'http://192.168.112.2:4444/wd/hub',
        #                    desired_capabilities=caps
        #                )
        self.logger = get_logger("sunnxt_homepage")
        self.logger.info("Launching {0} in {1} browswer ".format( website, 'chrome'))

        #self.home_url = website
        # driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

    def verify_profile_icon(self):
        try:
            browser = self.browser
            wait = WebDriverWait(browser, delay)
            self.logger.info("Verifying profile icon")
            ##profile_Elem = wait.until(
            ##    EC.presence_of_element_located((By.CLASS_NAME, 'icon-icn_profile'))
            ##)

            #find the profile element icon top right hand corner
            header_Elem = wait.until(
                EC.presence_of_element_located((By.XPATH, profile_icon_xpath))
            )
            #it's a javascript clickable element not a href tag
            browser.execute_script(js_click, header_Elem)
            self.logger.info("Found profile icon, sent click event")
        except TimeoutException as e:
            raise
        except Exception as e:
            raise    

    def verify_sigin_dropdown(self):

        try:
            browser = self.browser
            wait = WebDriverWait(browser, delay)
            self.logger.info("Verifying signin dropdown menu")

            #when the profile icon is clicked a drop down will show up
            #find the drop down element
            signin_Elem = wait.until(
                EC.presence_of_element_located((By.XPATH, signin_link_xpath))
            )

            #the dropdown has a text Sign In
            self.assertIn(signin_text, signin_Elem.get_attribute("text") )
            browser.execute_script(js_click, signin_Elem)
            self.logger.info("Found signin dropdown menu and sent click event")
            time.sleep(pause_delay)
            #browser.implicitly_wait(10)

        except TimeoutException as e:
            raise
        except Exception as e:
            raise        

    def verify_signin_modal_close_button(self):
        try:
            browser = self.browser
            wait = WebDriverWait(browser, delay)
            self.logger.info("Verifying signin modal window")
            
            #first find the x or close button in the right hand corner
            close_Elem = wait.until(
                EC.presence_of_element_located((By.XPATH, signin_modal_close_xpath))
            )
            browser.execute_script(js_click, close_Elem)
            time.sleep(pause_delay)
            self.logger.info("close button found and click event sent")
            
        except TimeoutException as e:
            raise
        except Exception as e:
            raise        

    def verify_signin_modal_title(self):
        try:
            browser = self.browser
            wait = WebDriverWait(browser, delay)
            self.logger.info("Verifying signin modal title")
            signin_title = wait.until(
                EC.presence_of_element_located((By.XPATH, signin_modal_title_xpath))
            )
            self.assertIn(signin_text, signin_title.get_attribute("innerText") )

        except TimeoutException as e:
            raise
        except Exception as e:
            raise   

    ###
    #  Fill in invalid details for the username/password ex username less than 8 characters
    #  expect errors to be trapped, no ajax request
    ###
    def verify_invalid_login_form(self):
        try:
            browser = self.browser
            wait = WebDriverWait(browser, delay)
            self.logger.info("Verifying form validations for signin")
            username_input = wait.until(
                EC.presence_of_element_located((By.XPATH, username_xpath))
            )
            self.assertIn(username_placeholder, username_input.get_attribute('placeholder') )

            self.logger.info("Verifying password input field")
            passwd_input = wait.until(
                EC.presence_of_element_located((By.XPATH, passwd_xpath))
            )
            self.assertIn(password_placeholder, passwd_input.get_attribute('placeholder') )
            username_input.clear()
            username_input.send_keys( invalid_user )
            passwd_input.clear()
            passwd_input.send_keys( invalid_password )

            submit_button = wait.until(
                EC.presence_of_element_located((By.XPATH, signin_button_xpath))
            )
            #print("Attribute", submit_button.get_attribute('class'))
            self.assertIn(btn_colors, submit_button.get_attribute('class') )
            submit_button.click()
            time.sleep(2)
            username_invalid_format = wait.until(
                EC.presence_of_element_located((By.XPATH, signin_invalid_format_xpath))
            )
            print("Attributes are ", username_invalid_format.get_attribute("innerText"), username_invalid_format.get_attribute("innerHTML") )
            self.assertIn(signin_invalid_user, username_invalid_format.get_attribute("innerText") )


        except TimeoutException as e:
            raise
        except Exception as e:
            raise   

    ###
    #  Fill in wrong credentials and expect errors to be trapped
    # here an ajax request will be made
    ###
    def verify_invalid_user_credentials(self):
        try:
            browser = self.browser
            wait = WebDriverWait(browser, delay)
            self.logger.info("Verifying Invalid user credentials")
            username_input = wait.until(
                EC.presence_of_element_located((By.XPATH, username_xpath))
            )
            self.assertIn(username_placeholder, username_input.get_attribute('placeholder') )

            self.logger.info("Verifying password input field")
            
            passwd_input = wait.until(
                EC.presence_of_element_located((By.XPATH, passwd_xpath))
            )

            self.assertIn(password_placeholder, passwd_input.get_attribute('placeholder') )
            
            username_input.clear()
            username_input.send_keys( invalid_username )

            passwd_input.clear()
            passwd_input.send_keys( invalid_passwd )

            #find the submit button
            submit_button = wait.until(
                EC.presence_of_element_located((By.XPATH, signin_button_xpath))
            )
            #verify that it is the correct button
            self.assertIn(btn_colors, submit_button.get_attribute('class') )
            self.logger.info("Sendinv invalid credentials")
            time.sleep(2)
            submit_button.click()
            submit_button.click()
            self.logger.info("Clicking login button ")

            time.sleep(2)
            #find an element with the error because wrong credentials were submitted
            wrong_credential = wait.until(
                EC.presence_of_element_located((By.XPATH, user_doesnot_exist_xpath))
            )
            print("Attributes are ", wrong_credential.get_attribute("innerText"), wrong_credential.get_attribute("innerHTML") )
            self.assertIn(verify_username_pwd, wrong_credential.get_attribute("innerText") )


        except TimeoutException as e:
            raise
        except Exception as e:
            raise   
        


    def test_homepage(self):
        browser = self.browser

        try:
            browser.get(website)
            self.verify_profile_icon()
            self.verify_sigin_dropdown()
            #self.verify_signin_modal_close_button()
            #self.verify_signin_modal_title()
            self.verify_invalid_login_form()
            self.verify_invalid_user_credentials()


        except TimeoutException as e:
            print("Timeout loading " + website )
            self.logger.exception(e)
        except Exception as e:
            self.logger.exception(e)


        ##try:

        ##except TimeoutException:
        ##     print("Timeout locating profile element in <" + self.home_url + ">")



    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()

