import os

import boto3
import botocore
import openai


ENDPOINT_URL = os.environ["ENDPOINT_URL"]
REGION_NAME = os.environ["REGION"]
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]



def main(event, _) -> None:
    audio_url = event.get("audio_url")
    print(audio_url)
    
    session = boto3.Session()
    client = session.client(
        's3',
        # Find your endpoint in the control panel, under Settings. Prepend "https://".
        endpoint_url=ENDPOINT_URL,
        # Use the region in your endpoint.
        region_name=REGION_NAME,
        # Access key pair. You can create access key pairs using the control panel or API.
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        # Secret access key defined through an environment variable.
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

