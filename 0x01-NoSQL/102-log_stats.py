#!/usr/bin/env python3
""" 12-log_stats.py"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Gets stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"""\tmethod {method}: {nginx.count_documents(
                {"method": method})}"""
              )
    print(f"""{nginx.count_documents({
            "method": "GET", "path": "/status"})} status check"""
          )

    print("IPs:")
    x = 0
    IPs_counter = nginx.aggregate([
        {
            '$group': {
                '_id': "$ip",
                'count': {'$sum': 1}
            }
        },
        {
            "$sort": {"count": -1}
        }
    ])

    for i in IPs_counter:
        print("\t{}: {}".format(i.get('_id'), i.get('count')))
        x += 1
        if x > 9:
            break