#!/usr/bin/python3
"""
100-my_int module
"""


class MyInt(int):
    def __eq__(self, other):
        """ Override the equal operator to return not equal """
        return super().__ne__(other)
    def __ne__(self, other):
        """ Override the not equal operator to return equal """
        return super().__eq__(other)
