from django.test import TestCase
from .models import Product
from rest_framework.test import APITestCase
import json

# Create your tests here.
class CheckProductAPITest(APITestCase):
    def test_register_product(self):
        product_1 = {'id': '1', 'fk_vendor':'1', 'name': 'test_product', 'price': '0.0', 'photo': 'test_photo', 'description': 'test_description'}

        #Checking POST
        first_response = self.client.post('/products/', product_1)
        self.assertEqual(first_response.status_code, 201)
        self.assertEqual(first_response.data["id"], int(product_1["id"]))
        self.assertEqual(first_response.data["fk_vendor"], int(product_1["fk_vendor"]))
        self.assertEqual(first_response.data["name"], product_1["name"])
        self.assertEqual(first_response.data["price"], float(product_1["price"]))
        self.assertEqual(first_response.data["photo"], product_1["photo"])
        self.assertEqual(first_response.data["description"], product_1["description"])

        #Checking GET
        get_response = self.client.get('/products/')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.data[0]["id"], int(product_1["id"]))
        self.assertEqual(get_response.data[0]["fk_vendor"], int(product_1["fk_vendor"]))
        self.assertEqual(get_response.data[0]["name"], product_1["name"])
        self.assertEqual(get_response.data[0]["price"], float(product_1["price"]))
        self.assertEqual(get_response.data[0]["photo"], product_1["photo"])
        self.assertEqual(get_response.data[0]["description"], product_1["description"])

    def test_products_get_details(self):
        product_1 = {'id': '1', 'fk_vendor':'1', 'name': 'test_product', 'price': '0.0', 'photo': 'test_photo', 'description': 'test_description'}

        #Check get one product
        first_response = self.client.post('/products/', product_1)
        get_response = self.client.get('/products/' + str(first_response.data['id']) + '/')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.data["id"], int(product_1["id"]))
        self.assertEqual(get_response.data["fk_vendor"], int(product_1["fk_vendor"]))
        self.assertEqual(get_response.data["name"], product_1["name"])
        self.assertEqual(get_response.data["price"], float(product_1["price"]))
        self.assertEqual(get_response.data["photo"], product_1["photo"])
        self.assertEqual(get_response.data["description"], product_1["description"])


    def test_product_delete(self):
        product_1 = {'id': '1', 'fk_vendor':'1', 'name': 'test_product', 'price': '0.0', 'photo': 'test_photo', 'description': 'test_description'}
        self.client.post('/products/', product_1)

        # FORBIDDEN if product request.fk_vendor != product.fk_vendor
        request_1 = {'fk_vendor': '2', 'product_id': '1'}
        second_response = self.client.post('/api/delete_product/', request_1)
        self.assertEqual(second_response.status_code, 403)

        # INTERNAL REQUEST ERROR if product does not exist
        request_2 = {'fk_vendor': '1', 'product_id': '3'}
        third_response = self.client.post('/api/delete_product/', request_2)
        self.assertEqual(third_response.status_code, 404)

        # BAD REQUEST if request has not fk_vendor or product_id
        request_3 = {'test': 'test'}
        fourth_response = self.client.post('/api/delete_product/', request_3)
        self.assertEqual(fourth_response.status_code, 400)

        # OK if product request.fk_vendor == product.fk_vendor and product exist
        request_4 = {'fk_vendor': '1', 'product_id': '1'}
        first_response = self.client.post('/api/delete_product/', request_4)
        self.assertEqual(first_response.status_code, 200)

    def test_product_create(self):
        # BAD REQUEST if price = 0
        product_1 = {'fk_vendor':'1', 'name': 'test_product', 'price': '0.0', 'photo': 'test_photo', 'description': 'test_description'}
        first_response = self.client.post('/api/create_product/', product_1)
        self.assertEqual(first_response.status_code, 400)

        # BAD REQUEST if any field is empty
        product_2 = {'test': 'test'}
        second_response = self.client.post('/api/create_product/', product_2)
        self.assertEqual(second_response.status_code, 400)

        #  Sucesses if can creat
        product_3 = {'fk_vendor':'1', 'name': 'test_product', 'price': '1.0', 'photo': 'test_photo', 'description': 'test_description'}
        third_response = self.client.post('/api/create_product/', product_3)
        self.assertEqual(third_response.status_code, 200)

    def test_user_products(self):
        request_1 = {'user_id':'1'}
        response_1 = self.client.post('/api/user_products/', request_1)
        self.assertEqual(response_1.status_code, 200)

        request_2 = {'user_id':'Errei'}
        response_2 = self.client.post('/api/user_products/', request_2)
        self.assertEqual(response_2.status_code, 400)

        request_3 = {'error':'testing'}
        response_3 = self.client.post('/api/user_products/', request_3)
        self.assertEqual(response_3.status_code, 400)

    def test_all_products(self):
        request_1 = {}
        response_1 = self.client.post('/api/all_products/', request_1)
        self.assertEqual(response_1.status_code, 200)

    def test_get_product(self):
        product_1 = {'id': '1', 'fk_vendor':'1', 'name': 'test_product', 'price': '0.0', 'photo': 'test_photo', 'description': 'test_description'}
        self.client.post('/products/', product_1)

        request_1 = {'product_id': '1'}
        response_1 = self.client.post('/api/get_product/', request_1)
        self.assertEqual(response_1.status_code, 200)

        request_2 = {'test': 'test'}
        response_2 = self.client.post('/api/get_product/', request_2)
        self.assertEqual(response_2.status_code, 400)

        request_3 = {'product_id': ''}
        response_3 = self.client.post('/api/get_product/', request_3)
        self.assertEqual(response_3.status_code, 400)

        request_4 = {'product_id': '2'}
        response_4 = self.client.post('/api/get_product/', request_4)
        self.assertEqual(response_4.status_code, 400)
