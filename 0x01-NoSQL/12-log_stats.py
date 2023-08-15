#!/usr/bin/env python3
"""A python script that pprovides some stats about Nginx logs"""
from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.logs.nginx
    num = school_collection.count_documents({})
    print(f"{num} logs")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for met in method:
        print("\tmethod {}: {}".format(met, school_collection.count_documents({"met": met})))
    num2 = school_collection.count_documents({"path": "/status"})
    print(f"{num2} status check")