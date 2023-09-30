"""This is an test of app:notify trash pickup date."""

# pylint disable=missing-function-docstring

import trash_notification as tn


def test_get_region_list():

    filepath = '/home/nee/git/notification_trash_pickup_day/input/2023/db_region_to_regioncode.csv'
    s_region = tn.get_region_list(filepath)

    assert len(s_region) == 53
