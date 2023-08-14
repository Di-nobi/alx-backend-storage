#!/usr/bin/env python3
"""Mongodb with Python"""

def list_all(mongo_collection):
    """lists all documents in Python"""
    doc = mongo_collection.find()

    if not doc:
        return []
    return doc