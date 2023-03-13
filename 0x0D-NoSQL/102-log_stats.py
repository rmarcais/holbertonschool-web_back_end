#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient, DESCENDING

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    documents = nginx_collection.count_documents({})
    print("{} logs".format(documents))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("    method {}: {}".format(
            method,
            nginx_collection.count_documents({"method": method})
        ))

    print("{} status ckeck".format(
        nginx_collection.count_documents({"$and": [{"path": "/status"},
                                                   {"method": "GET"}]})
    ))

    pipeline = [
            {
                "$group": {
                    "_id": "$ip",
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "count": DESCENDING
                }
            },
            {
                "$limit": 10
            }
        ]

    print("IPs:")
    result = list(nginx_collection.aggregate(pipeline))
    for item in result:
        print("    {} {}".format(item.get("_id"), item.get("count")))
