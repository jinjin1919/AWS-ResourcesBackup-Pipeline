#  Copyright 2016 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

import urllib3
import json
http = urllib3.PoolManager()
SUCCESS = "SUCCESS"
FAILED = "FAILED"


def send(event, context, responseStatus, responseData, physicalResourceId=None, noEcho=False):

    try:
        responseUrl = event['ResponseURL']

        responseBody = {}
        responseBody['Status'] = responseStatus
        responseBody['Reason'] = 'See the details in CloudWatch Log Stream: ' + \
            context.log_stream_name
        responseBody['PhysicalResourceId'] = physicalResourceId or context.log_stream_name
        responseBody['StackId'] = event['StackId']
        responseBody['RequestId'] = event['RequestId']
        responseBody['LogicalResourceId'] = event['LogicalResourceId']
        responseBody['NoEcho'] = noEcho
        responseBody['Data'] = responseData

        json_responseBody = json.dumps(responseBody)

        headers = {
            'content-type': '',
            'content-length': str(len(json_responseBody))
        }

        response = http.request(
            'PUT', responseUrl, body=json_responseBody.encode('utf-8'), headers=headers)
        print("Status code: " + response.reason)

    except Exception as e:
        pass
