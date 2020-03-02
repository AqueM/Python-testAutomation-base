from random import randint, choice

import unittest


def get_data_from_csv(file):
    # grabs a random row from file and returns its contents as list
    with open(file) as f:
        data_list = f.read().splitlines()
        data_list.pop(0)
        my_pick = choice(data_list)
        data = my_pick.split(',')
    return data


def get_valid_user():
    return get_data_from_csv(TestData.valid_users)


class TestData(unittest.TestCase):
    valid_users = "../resources/test_data/valid_users.csv"
