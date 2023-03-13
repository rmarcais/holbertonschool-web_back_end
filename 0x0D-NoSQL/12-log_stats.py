#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    documents = nginx_collection.count_documents({})
    print("{} logs".format(documents))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(
            method,
            nginx_collection.count_documents({"method": method})
        ))

    print("{} status check".format(
        nginx_collection.count_documents({"$and": [{"path": "/status"},
                                                   {"method": "GET"}]})
    ))
