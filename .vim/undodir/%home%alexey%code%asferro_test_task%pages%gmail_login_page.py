Vim�UnDo� �?8�|SY��"�4i���+��-�1������~5                    -       -   -   -    aA�    _�                             ����                                                                                                                                                                                                                                                                                                                                                            aA��     �                   5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                            aA��     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �                 Cfrom utils.locators import MainPageLocators, GmailLoginPageLocators5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��    �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��    �               �   
                     self.wait_element()�   	                     sign_in.click()�      
          :        sign_in = self.find_element(*self.locator.SIGN_IN)�      	              def check_login(self):�                 �                4        super(GmailLoginPage, self).__init__(driver)�                -        self.locator = GmailLoginPageLocators�                    def __init__(self, driver):�                class GmailLoginPage(BasePage):�                1from utils.locators import GmailLoginPageLocators�                 $from pages.base_page import BasePage5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �   
                    �   
          5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�    �               :        sign_in = self.find_element(*self.locator.SIGN_IN)5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�A     �               >        sign_in = self.find_element(*self.locator.EMAIL_INPUT)5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�O     �                       sign_in.click()5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�Y     �                         self.wait_element()5�_�   
                    5    ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�x     �                         �               5�_�                       F    ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �                         �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �                       email_input.click()5�_�                          ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �      	                 �      	       5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��    �      
                 �      
       5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�     �      	                 self._login = 5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�    �      	                 self._login = ""�      	       5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�     �      
                 self._password = �   	   
       5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�     �      
         '        self._password =  "qwerty11235"5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�(     �                       email_input.send_keys5�_�                           ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�1     �                       password_input.click()5�_�                       )    ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�K     �                       �             5�_�                       =    ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA�d     �                       �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                               v       aA�v     �                       CONTINUE_BUTTON_LOGIN5�_�                           ����                                                                                                                                                                                                                                                                                                                                               v       aA�w     �                       continue_button_login5�_�                       T    ����                                                                                                                                                                                                                                                                                                                                               v       aA     �                       �             5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                               v       aA     �                       �             5�_�                        ?    ����                                                                                                                                                                                                                                                                                                                                               v       aA¥     �                       �             5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                               v       aA­     �                        CONTINUE_BUTTON_PASSWORD5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                               v       aA®     �                        continue_button_password5�_�   !   #           "      Z    ����                                                                                                                                                                                                                                                                                                                                               v       aAº    �                       �             5�_�   "   $           #      &    ����                                                                                                                                                                                                                                                                                                                                               v       aA��    �               �                 �                (        continue_button_password.click()�                \        continue_button_password = self.find_element(*self.locator.CONTINUE_BUTTON_PASSWORD)�                A        self.wait_element(*self.locator.CONTINUE_BUTTON_PASSWORD)�                0        password_input.send_keys(self._password)�                H        password_input = self.find_element(*self.locator.PASSWORD_INPUT)�                7        self.wait_element(*self.locator.PASSWORD_INPUT)�                %        continue_button_login.click()�                V        continue_button_login = self.find_element(*self.locator.CONTINUE_BUTTON_LOGIN)�                >        self.wait_element(*self.locator.CONTINUE_BUTTON_LOGIN)�                *        email_input.send_keys(self._login)�                B        email_input = self.find_element(*self.locator.EMAIL_INPUT)�                4        self.wait_element(*self.locator.EMAIL_INPUT)�                    def check_login(self):�   
              �   	             4        super(GmailLoginPage, self).__init__(driver)�      
          &        self._password = "qwerty11235"�      	          4        self._login = "testingqwerty11235@gmail.com"�                -        self.locator = GmailLoginPageLocators�                    def __init__(self, driver):�                class GmailLoginPage(BasePage):�                 �                 �                1from utils.locators import GmailLoginPageLocators�                 $from pages.base_page import BasePage5�_�   #   %           $           ����                                                                                                                                                                                                                                                                                                                                                            aA��     �             5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                                                            aA��     �                �             5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                                                            aA��     �               H        password_input = self.find_element(*self.locator.PASSWORD_INPUT)    �                5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                                                            aA��     �               from time import time5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                            aA�   	 �                       �             5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                                                 V        aA�(   
 �                A        self.wait_element(*self.locator.CONTINUE_BUTTON_PASSWORD)�                7        self.wait_element(*self.locator.PASSWORD_INPUT)�                >        self.wait_element(*self.locator.CONTINUE_BUTTON_LOGIN)�                4        self.wait_element(*self.locator.EMAIL_INPUT)5�_�   )   +           *           ����                                                                                                                                                                                                                                                                                                                                                            aA�S    �                        time.sleep(2)5�_�   *   ,           +           ����                                                                                                                                                                                                                                                                                                                                                            aA�x    �                         �               5�_�   +   -           ,      +    ����                                                                                                                                                                                                                                                                                                                                                            aA��     �                 ,        assert self.get_element_if_located()5�_�   ,               -      '    ����                                                                                                                                                                                                                                                                                                                                                            aA�    �             5�_�                          ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �                �               import config5�_�                            ����                                                                                                                                                                                                                                                                                                                                        ,       v   ,    aA��     �               &        email_input.send_keys(config.)5��