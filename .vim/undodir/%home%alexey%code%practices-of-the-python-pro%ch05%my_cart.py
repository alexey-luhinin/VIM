Vim�UnDo� 7,�t�~^݋@ߏ�����*���r����              *                       a�    _�                        *    ����                                                                                                                                                                                                                                                                                                                                                             a��    �               /        if self.products[sku]['quantity'] == 0:5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             a��    �                        """�                "            del self.products[sku]�                /        if self.products[sku]['quantity'] <= 0:�                        To fix the bug:�                        """�                 �                "            del self.products[sku]�                /        if self.products[sku]['quantity'] <= 0:�                2        self.products[sku]['quantity'] -= quantity�                $        sku = product.generate_sku()�   
             9    def remove_product(self, product, quantity=1):  # <3>�   	              �      
          E        self.products[product.generate_sku()]['quantity'] += quantity�      	          6    def add_product(self, product, quantity=1):  # <2>�                 �                D        self.products = defaultdict(lambda: defaultdict(int))  # <1>�                    def __init__(self):�                class ShoppingCart:�                 �                 �                 #from collections import defaultdict5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        a�     �                        """           To fix the bug:   /        if self.products[sku]['quantity'] <= 0:   "            del self.products[sku]           """5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        a�    �                 5��