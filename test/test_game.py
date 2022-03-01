#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig Dice Game Unittesting."""

import unittest
from game import game


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = game.Game()
        exp = game.Game
        self.assertIsInstance(res, exp)


if __name__ == "__main__":
    unittest.main()
