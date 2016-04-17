# Copyright 2015 Furtivio LLC
# Licensed under the Apache License, Version 2.0 (see LICENSE).


import unittest

from furtivio.example.helloworld import HelloWorld


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.hw = HelloWorld()

    def test_hello(self):
        self.assertEqual(self.hw.hello(), HelloWorld.GREETING)
