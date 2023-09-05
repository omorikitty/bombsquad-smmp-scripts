# coding: utf-8
import json
import os
import time
import sys
import bs


SETTING_PATH = os.path.abspath(os.path.join(
    bs.getEnvironment().get('userScriptsDirectory'), 'settings.json'))


def get_setting():
    try:
        with open(SETTING_PATH, mode='r') as f:
            return json.load(f)
    except:
        raise Exception("settings.json does not exist")


def commit(d):
    with open(SETTING_PATH, mode='w') as f:
        json.dumps(f, d, indent=4)


def check_setting():
    if os.path.exists(SETTING_PATH):
        print('settings.json file is ready all in order!')
    else:
        print('settings.json file does not exist exiting...')
        sys.exit()


check_setting()
