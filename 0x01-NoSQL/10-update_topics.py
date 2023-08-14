#!/usr/bin/env python3
""" Changes the topic of a school"""
def update_topics(mongo_collection, name, topics):
    """Changes the topic of a school"""
    doc = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return doc