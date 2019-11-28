import pymongo
import sys
import datetime
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson import json_util


def get_data(event, context):
    # Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
    username = "chamseddine"
    password = "123456chams"
    db_cluster = "cloud-concordia"
    client = pymongo.MongoClient(
        f'mongodb://{username}:{password}@{db_cluster}.cluster-cxfjdmvmj3tw.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0')

    # Specify the database to be used
    db = client.test

    # Specify the collection to be used
    col = db.datas

    uid = event['pathParameters']['user']

    data = col.find({"correspond": ObjectId(uid)})
    data = list(data)
    for dt in data:
        temp_date = dt['date']
        dt['date'] = "{}-{}-{}".format(temp_date.year,
                                       temp_date.month, temp_date.day)

    # Close the connection
    client.close()
    # print(list(data))
    # data=json.dumps(data,default=json_util.default)
    return {'statusCode': 200,
        'body': dumps(data)}
    # return context
