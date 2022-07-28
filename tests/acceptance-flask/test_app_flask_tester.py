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
