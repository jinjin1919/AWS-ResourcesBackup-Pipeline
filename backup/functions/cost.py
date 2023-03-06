import csv
from datetime import datetime


class Cost:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def get_cost_and_usage(self, tag):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")

        response = self.client.get_cost_and_usage(
            TimePeriod={
                'Start': '2022-01-01',
                'End': date
            },
            Granularity='MONTHLY',
            Metrics=[
                'UnblendedCost',
            ],
            Filter={
                'And': [{
                    'Dimensions': {
                        'Key': 'SERVICE',
                        'Values': ['AWS Backup']
                    }
                }, {
                    'Not': {
                        'Dimensions': {
                            'Key': 'RECORD_TYPE',
                            'Values': ['Refund', 'Credit']
                        }
                    }
                }]
            },
            GroupBy=[
                {
                    'Type': 'TAG',
                    'Key': tag
                },
            ],
        )

        return response

    def get_cost_by_tags(self, tags):
        cost_data = []
        for tag in tags:
            response = self.get_cost_and_usage(tag)
            size = len(response['ResultsByTime'])

            for i in range(size):
                estimate = response['ResultsByTime'][i]['Estimated']
                if (not estimate):
                    row = []
                    start = response['ResultsByTime'][i]['TimePeriod']['Start']
                    end = response['ResultsByTime'][i]['TimePeriod']['End']

                    if len(response['ResultsByTime'][i]['Groups']) == 0:
                        tag_response = " "
                        unblendedcost = float(
                            response['ResultsByTime'][i]['Total']['UnblendedCost']['Amount'])
                    else:
                        tag_response = response['ResultsByTime'][i]['Groups'][0]['Keys'][0][:-1]
                        unblendedcost = float(
                            response['ResultsByTime'][i]['Groups'][0]['Metrics']['UnblendedCost']['Amount'])

                    row = [start, end, tag_response, unblendedcost]
                    cost_data.append(row)

        self.write_to_csv(cost_data)

    def write_to_csv(self, cost_data):

        csv_file = open('cost.csv', 'w')
        csv_writer = csv.writer(csv_file)

        header = ["StartDate", "EndDate", "Tags", "UnblendedCost"]
        csv_writer.writerow(header)
        csv_writer.writerows(cost_data)

        csv_file.close()
