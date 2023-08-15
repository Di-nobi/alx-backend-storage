#!/usr/bin/env python3
""" A python function that returns all students sorted by average score"""
def top_students(mongo_collection):
    """Returns all students sorted by the average"""
    students = mongo_collection.aggregate([
        {
            "$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}
        },
        {
            "$sort": {"averageScore": -1}
        }

    ])
    return students