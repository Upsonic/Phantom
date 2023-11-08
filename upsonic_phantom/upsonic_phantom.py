#!/usr/bin/python3
# -*- coding: utf-8 -*-

from upsonic import Upsonic, Upsonic_Remote, HASHES


class Upsonic_Phantom:
    def __init__(self, cloud, encryption_key="a") -> None:
        self.cloud = cloud
        self.encryption_key = encryption_key

    def register(self, function):
        self.cloud.active(value=function, encryption_key=self.encryption_key)

    def use(self, name):
        return self.cloud.get(name, encryption_key=self.encryption_key)
