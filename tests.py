# -*- coding: utf-8 -*-
import unittest
from app import app as myapp


class TestMyApp(unittest.TestCase):

    def setUp(self):
        self.app = myapp.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'Hello' in rv.data

    def test_404(self):
        rv = self.app.get('/unknown')
        self.assertEqual(rv.status, '404 NOT FOUND')


if __name__ == '__main__':
    unittest.main()
