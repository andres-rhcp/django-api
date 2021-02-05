from django.test import TestCase


class TestProductManage(TestCase):
    """
    Class used to test driven development cases
    """

    def test_create_product(self):
        """
        Tests insert data to product table
        """        
        data = {
            "product_sku": "003",
            "product_name": "tuna",
            "product_type": "tuna 001",
            "stock": 5,
            "date_update": "04-02-2020",
            "user_update": "andres",
            "observation": "none"
        }        
        response = self.client.get(self.url, data)
        self.assertContains(response, 'ok')


