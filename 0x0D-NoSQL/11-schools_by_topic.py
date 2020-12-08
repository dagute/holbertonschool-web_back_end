#!/usr/bin/python3
"""Where can I learn Python"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having specific topic"""
    return mongo_collection.find({"topics": topic})