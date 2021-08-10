# Some prerequisites are needed
# To execute in your gcloud environment run the line below
# python gcp_list_vms.py <your-key.json>
from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

import googleapiclient.discovery
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<jsonpath> eg. /home/bootcamper/key-automation.json"

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'your-project-id bootcamp-challenge1'
zone =  'your-zone eg. us-east1-b'

compute = googleapiclient.discovery.build('compute', 'v1')

# [START list_instances]
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()

    for item in result['items']:
        if item['status'] == "RUNNING":
            print (item['name'])
# [END list_instances]


list_instances(compute,project, zone)
print('done')

