#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    documents = nginx_collection.count_documents({})
    print("{} logs".format(documents))

    print("Methods:")
    print("method GET: {}".format(
        nginx_collection.count_documents({"method": "GET"})
    ))
    print("method POST: {}".format(
        nginx_collection.count_documents({"method": "POST"})
    ))
    print("method PUT: {}".format(
        nginx_collection.count_documents({"method": "PUT"})
    ))
    print("method PATCH: {}".format(
        nginx_collection.count_documents({"method": "PATCH"})
    ))
    print("method DELETE: {}".format(
        nginx_collection.count_documents({"method": "DELETE"})
    ))

    print("{} status ckeck".format(
        nginx_collection.count_documents({"$and": [{"path": "/status"},
                                                   {"method": "GET"}]})
    ))
