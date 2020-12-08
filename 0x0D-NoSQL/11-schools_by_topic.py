#!/usr/bin/python3
"""Where can I learn Python"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having specific topic"""
    docs = mongo_collection.find({"topics": topic})
    _lists = [x for x in docs]
    return _lists
