#!/usr/bin/env python3
import pymongo
"""A python function that returns the list of school having a specific topic"""
def schools_by_topic(mongo_collection, topic):
    """Lists schools of specific topics"""
    doc = mongo_collection.find({"topics": topic})
    return doc