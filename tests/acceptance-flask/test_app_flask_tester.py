import json
import unittest
from project import app 

class TestApp(unittest.TestCase):

    token=''
   
    def test_1_getToken(self):         
        self.assertTrue(True)

        tester = app.test_client(self)

        user_data = {"email":"jd@myinsuranceapp.com","password":"passwordjd"}

        response = tester.post('/api/v1/token', content_type='application/json', json = user_data)

        data=json.loads(response.text)

        print(f"post token: {data}")

        self.assertEqual(response.status_code, 200)

        if response.status_code==200:
            TestApp.token=data['token']
            
    def test_2_get_user_products_valid_token(self):
        tester = app.test_client(self)

        print(f"token: {self.token}")

        headers = {"Authorization": f"Bearer {TestApp.token}"}

        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)

        data=json.loads(response.text)
        print(f"get_user_products: {data}")
        self.assertEqual(response.status_code, 200)

        self.assertTrue(len(data)>0)

    def test_3_get_user_products_invalid_token(self):
        tester = app.test_client(self)
        
        ivalid_fake_token='CfDJ8OW5OI0CPGJBgSNlGwO0x4YF7qbYKVv7KOO-N0eFtDUzXOrL7F9Xd9W1otVi4ueJOkAmAhuoHFWNkqRaFD7zvAMHMSKncl6Vo5QXKmpvy6vqxOKxSURdIey8aZPRi3Nnhp2p9la-Al5xrVKz0lignRdcCHf3O7pF9zv_sNx_c_T7pUe3WsxaJEPX3t_9FO2Wjw'

        headers = {"Authorization": f"Bearer {ivalid_fake_token}"}
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)
        data=json.loads(response.text)
        print(f"get_user_products: {data}")

        self.assertTrue(response.status_code > 400)


    def test_4_invalid_user(self):
        tester = app.test_client(self)

        print(f"token: {self.token}")

        headers = {"Authorization": f"Bearer {TestApp.token}"}

        response = tester.get('/api/v1/users/89/products', content_type='application/json', headers=headers)

        data=json.loads(response.text)
        """self.assertTrue(response.status_code > 400)"""
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 0)


    def test_5_product(self):
        tester = app.test_client(self)

        print(f"token: {self.token}")

        headers = {"Authorization": f"Bearer {TestApp.token}"}

        response = tester.get('/api/v1/products/1', content_type='application/json', headers=headers)
        print(response)
        data=json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)
"""
    def test_5_product(self):
        tester = app.test_client(self)

        print(f"token: {self.token}")

        headers = {"Authorization": f"Bearer {TestApp.token}"}

        response = tester.get('/api/v1/products/6', content_type='application/json', headers=headers)
        print(response)
        data=json.loads(response.text)
        print(data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)
"""