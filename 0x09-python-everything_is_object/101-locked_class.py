!/usr/bin/python3
"""LockedClass class"""


class LockedClass:
    """LockedClass class to prevent creating new instance attributes"""
    __slots__ = ['first_name']
