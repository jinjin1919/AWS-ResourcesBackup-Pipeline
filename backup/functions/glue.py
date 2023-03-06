import csv
import boto3


class Glue:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def create_table(self, table_name, database_name, column, location):

        try:
            response = self.client.create_table(
                CatalogId=self.account_id,
                DatabaseName=database_name + self.account_id,
                TableInput={
                    'Name': table_name,
                    'StorageDescriptor': {
                        'Columns': column,
                        'Location': location,
                        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                        'SerdeInfo': {
                            'Parameters': {
                                'case.insensitive': 'true',
                                'field.delim': ',',
                                'skip.header.line.count': '1',
                            },
                            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
                        },
                        'BucketColumns': [],
                    },
                    'Parameters': {
                        'classification': 'csv',
                        'typeOfData': 'file'
                    }
                },
            )
        except:
            response = self.client.update_table(
                CatalogId=self.account_id,
                DatabaseName=database_name + self.account_id,
                TableInput={
                    'Name': table_name,
                    'StorageDescriptor': {
                        'Columns': column,
                        'Location': location,
                        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                        'SerdeInfo': {
                            'Parameters': {
                                'case.insensitive': 'true',
                                'field.delim': ',',
                                'skip.header.line.count': '1',
                            },
                            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
                        },
                        'BucketColumns': [],
                    },
                    'Parameters': {
                        'classification': 'csv',
                        'typeOfData': 'file'
                    }
                },
            )
