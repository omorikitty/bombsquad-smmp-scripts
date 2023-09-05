# -*- coding: utf-8 -*-
import bs
import bsLobby
from bsLobby import Chooser


def _set_ready(func):
    def deco(*args, **kwargs):
        func(*args, **kwargs)
        clientID = args[0]._player.getInputDevice().getClientID()
        if args[0].ready:
            bs.screenMessage(u'~ Hello ~', color=(0.5, 0.7, 0.8),
                             transient=True, clients=[clientID])

    return deco


def main():
    Chooser._setReady = _set_ready(Chooser._setReady)
