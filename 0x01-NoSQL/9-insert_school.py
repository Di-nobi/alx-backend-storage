#!/usr/bin/env python3
"""A python function that inserts a new document in a collections based kwargs"""
def insert_school(mongo_collection, **kwargs):
    """Inserts the new document in a collection"""
    doc_id =  mongo_collection.insert(kwargs)
    return doc_id