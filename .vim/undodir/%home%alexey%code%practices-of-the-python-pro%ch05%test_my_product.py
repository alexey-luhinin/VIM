Vim�UnDo� �S���ֶ�������,֩�Z0p��߀���r              expected = "HAT-M-RED"            (   (   (   (   '    a�b    _�                             ����                                                                                                                                                                                                                                                                                                                                                             a�     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a�     �                  �               5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                             a��     �                 (class ProductTestCase(unittest.TestCase)5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                             a��    �                     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a��    �               �                    pass�                )class ProductTestCase(unittest.TestCase):�                 �                 import unittest5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a�     �                     pass5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             a�    �                         �               5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                V       a�     �                    def test_working(self):           pass5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                V       a�     �                     �               5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                V       a�     �                 &    test_transform_name_for_sku(self):5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                V       a�!     �                         �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�A    �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�T     �                         5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�n     �                       �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       a�     �               *        test_product = Product("one", "M")5�_�                       )    ����                                                                                                                                                                                                                                                                                                                                                V       a�     �               *        test_product = Product("hat", "M")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�    �                        self.assertEqual() 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�     �             5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                V       a�     �                        self.assertEqual(t) 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       a�    �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�   	 �      	                  self.assertEqual(t) �                1        test_product = Product("hat", "M", "red")�                *    def test_transform_name_for_sku(self):�                )class ProductTestCase(unittest.TestCase):�                 �                 �                from my_product import Product�                 import unittest5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�    �                         self.assertEqual(t)5�_�                       C    ����                                                                                                                                                                                                                                                                                                                                                V       a�N     �                         �               5�_�                    
   *    ����                                                                                                                                                                                                                                                                                                                                                V       a�`     �   
            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�f     �                1        test_product = Product("hat", "M", "red")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�f     �         
    �         
    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�g     �               1        test_product = Product("hat", "M", "red")5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                V       a�i    �   
                    �   
          5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       a�k    �                 �   
                     pass�   	             +    def test_transform_color_for_sku(self):�      
           �      	          F        self.assertEqual(test_product.transform_name_for_sku(), "HAT")�                *    def test_transform_name_for_sku(self):�                -    test_product = Product("hat", "M", "red")�                )class ProductTestCase(unittest.TestCase):�                 �                 �                from my_product import Product�                 import unittest5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                V       a�v    �      
         F        self.assertEqual(test_product.transform_name_for_sku(), "HAT")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       a�    �                         pass5�_�      !                  I    ����                                                                                                                                                                                                                                                                                                                                                V       a��     �                         �               5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                V       a��     �                         �               5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                V       a�      �                         �               5�_�   "   $           #      9    ����                                                                                                                                                                                                                                                                                                                                                V       a�6    �                 :        self.assertEqual(self.test_product.generate_sku())5�_�   #   %           $      *    ����                                                                                                                                                                                                                                                                                                                                                V       a�D     �                       �             5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                V       a�J     �      
                 �      
       5�_�   %   '           &   
   D    ����                                                                                                                                                                                                                                                                                                                                                V       a�S     �   	            K        self.assertEqual(self.test_product.transform_name_for_sku(), "HAT")5�_�   &   (           '      E    ����                                                                                                                                                                                                                                                                                                                                                V       a�W    �               L        self.assertEqual(self.test_product.transform_color_for_sku(), "RED")5�_�   '               (          ����                                                                                                                                                                                                                                                                                                                                                V       a�b    �                       expected = "HAT-M-REd"5��