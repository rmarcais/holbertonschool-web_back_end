#!/usr/bin/env python3
"""101-students module"""

import pymongo


def top_students(mongo_collection):
    """Returns all students sorted bu average score"""
    pipeline = [
            {
                "$project": {
                    "name": 1, "averageScore": {"$avg": "$topics.score"}
                }
            },
            {
                "$sort": {
                    "averageScore": pymongo.DESCENDING
                }
            }
        ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
