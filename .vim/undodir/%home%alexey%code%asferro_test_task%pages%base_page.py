Vim�UnDo� �B82����N{8����ʋ
0k<�-#@z�?/   $                       5       5   5   5    aA؟    _�                             ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                   5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             a@�     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             a@�     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a@�     �                     �               5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                 +    def __init__(self, driver, base_url="")�               5�_�      	                 V    ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                 V    def __init__(self, driver, base_url="https://www.google.com/intl/en/gmail/about/")5�_�      
           	      V    ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                         �               5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                         �               5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             a@��    �                         �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a@��    �               �      	                  self.timeout = 25�                        self.driver = driver�                         self.base_url = base_url�                W    def __init__(self, driver, base_url="https://www.google.com/intl/en/gmail/about/"):�                class BasePage(object):�                 �                @from selenium.webdriver.support import expected_conditions as EC�                 7from selenium.webdriver.support.ui import WebDriverWait5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             a@�$     �   	                      �   	            5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             a@�:     �                         �               5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             a@�E     �                     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a@�K     �                         �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a@�U     �                         �               5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             a@�p     �                 $    def wait_element(self, *locator)5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             a@�q     �                         �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a@�s     �                             �               5�_�                       V    ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                             �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                             �               5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                 9            print("Can't find element by locator".format)5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                                                             a@��     �                 <            print("Can't find element by locator {}".format)5�_�                       D    ����                                                                                                                                                                                                                                                                                                                                                             a@��    �                             �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a@��    �               �                            self.driver.quit()�                H            print("Can't find element by locator {}".format(locator[1]))�                         except TimeoutException:�                Y            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))�                        try:�                %    def wait_element(self, *locator):�                 �                        self.driver.get(url)�                    def open(self, url):�                 �                1        return self.driver.find_element(*locator)�   
             %    def find_element(self, *locator):�   	              �      
                  self.timeout = 25�      	                  self.driver = driver�                         self.base_url = base_url�                W    def __init__(self, driver, base_url="https://www.google.com/intl/en/gmail/about/"):�                class BasePage(object):�                 �                 �                @from selenium.webdriver.support import expected_conditions as EC�                 7from selenium.webdriver.support.ui import WebDriverWait5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             a@�*    �                 �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             aA�     �               W    def __init__(self, driver, base_url="https://www.google.com/intl/en/gmail/about/"):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             aA�     �                         self.base_url = base_url5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                             aA�   
 �               1            WebDriverWait(self.driver, 20).until(5�_�      #                      ����                                                                                                                                                                                                                                                                                                                                                             aA��    �               ;            WebDriverWait(self.driver, self.timeout).until(5�_�      $           #      /    ����                                                                                                                                                                                                                                                                                                                                                             aAĊ    �               7                EC.presence_of_element_located(locator)5�_�   #   %           $      /    ����                                                                                                                                                                                                                                                                                                                                                             aA��    �               8                EC.presence_of_element_located(*locator)5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             aAƒ     �               %    def wait_element(self, *locator):5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             aAƟ     �                             �               5�_�   &   (           '      0    ����                                                                                                                                                                                                                                                                                                                                                             aA��     �                 0    def get_element_if_clickable(self, *locator)5�_�   '   )           (      0    ����                                                                                                                                                                                                                                                                                                                                                             aA��     �               5�_�   (   ,           )           ����                                                                                                                                                                                                                                                                                                                                                V       aA��     �      "       �             5�_�   )   -   *       ,          ����                                                                                                                                                                                                                                                                                                                                                V       aA��     �         "      ;            WebDriverWait(self.driver, self.timeout).until(5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                V       aA��    �         "      7                EC.presence_of_element_located(locator)5�_�   -   /           .      )    ����                                                                                                                                                                                                                                                                                                                                                V       aA�
    �   !               �       "                      self.driver.quit()�      !          H            print("Can't find element by locator {}".format(locator[1]))�                          except TimeoutException:�                            )�                3                EC.element_to_be_clickable(locator)�                B            return WebDriverWait(self.driver, self.timeout).until(�                        try:�                1    def get_element_if_clickable(self, *locator):�                 �                            self.driver.quit()�                H            print("Can't find element by locator {}".format(locator[1]))�                         except TimeoutException:�                            )�                7                EC.presence_of_element_located(locator)�                ;            WebDriverWait(self.driver, self.timeout).until(�                        try:�                %    def wait_element(self, *locator):�                 �                        self.driver.get(url)�                    def open(self, url):�                 �                1        return self.driver.find_element(*locator)�   
             %    def find_element(self, *locator):�   	              �      
                  self.timeout = 25�      	                  self.driver = driver�                    def __init__(self, driver):�                class BasePage(object):�                 �                 �                @from selenium.webdriver.support import expected_conditions as EC�                7from selenium.webdriver.support.ui import WebDriverWait�                 7from selenium.common.exceptions import TimeoutException5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                V       aA�]     �         !      %    def wait_element(self, *locator):5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                v       aA�d     �         !      3    def get_element_ifwait_element(self, *locator):5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                v       aA�g     �         !      0    def get_element_ifl_element(self, *locator):5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                v       aA�g     �         !      /    def get_element_if_element(self, *locator):5�_�   2   4           3          ����                                                                                                                                                                                                                                                                                                                                                v       aA�v    �         !      ;            WebDriverWait(self.driver, self.timeout).until(5�_�   3   5           4           ����                                                                                                                                                                                                                                                                                                                                                             aAؒ     �         "          �         !    5�_�   4               5      %    ����                                                                                                                                                                                                                                                                                                                                                             aA؞    �         $              �         #    5�_�   )   +       ,   *          ����                                                                                                                                                                                                                                                                                                                                                V       aA��     �         "      E            element = WebDriverWait(self.driver, self.timeout).until(5�_�   *               +          ����                                                                                                                                                                                                                                                                                                                                                V       aA��     �         "                  �          #                  return 5�_�      !       #              ����                                                                                                                                                                                                                                                                                                                                                             aA��    �               E            element = WebDriverWait(self.driver, self.timeout).until(5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             aA��     �                           �                           return element5�_�   !               "          ����                                                                                                                                                                                                                                                                                                                                                             aA�     �                            �                        def send_keys(self, )5��