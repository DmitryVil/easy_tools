from urllib.parse import urlparse
from pickle import dumps, loads
import pandas as pd
import boto3
from data_access.handlers.__class_abstract_handler import AbstractHandler


class S3(AbstractHandler):
    cloud_client = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url_parse = urlparse(self.link)
        self.s3_bucket = self.url_parse.netloc
        self.key = self.url_parse.path
        self.s3_client = self.get_create_s3_client()

    def get(self):
        s3_response_object = self.s3_client.get_object(Bucket=self.s3_bucket, Key=self.key)
        return loads(s3_response_object['Body'].read())

    def put(self, data: pd = None):
        self.s3_client.put_object(Body=dumps(data), Bucket=self.s3_bucket, Key=self.key)

    @classmethod
    def get_create_s3_client(cls):
        if cls.cloud_client is None:
            cls.cloud_client = boto3.client('s3')
        return cls.cloud_client



