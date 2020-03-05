from django.test import TestCase

# Create your tests here.
class  UserTestCase(TestCase):
    def SetUp(self):
        pass

    def test_my_func(self):
        response = self.client.get('login/')
        self.assertEquals(response.status_code, 200)

class  UserTestCase2(TestCase):
    def test_my_func2(self):

        post_user_session_data = {
            'username': 'xiaofeng',
            'password': 'Xf19991117.'
        }

        response = self.client.post("login/", data=post_user_session_data)
        self.assertEqual(response.status_code, 200)
