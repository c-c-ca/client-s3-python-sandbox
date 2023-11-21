import os
from os.path import join, dirname
from dotenv import load_dotenv

import time

import boto3


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
REGION = os.environ.get("REGION")
BUCKET_NAME = os.environ.get("BUCKET_NAME")

FILENAME_SUFFIX = "image_capture"
FILETYPE = "png"
IMAGE_FILEPATH = join(dirname(__file__), "images", "code-snippet-screenshot.png")


def main():
    s3 = boto3.client(
        "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
    )

    with open(IMAGE_FILEPATH, "rb") as f:
        response = s3.put_object(
            Bucket=BUCKET_NAME,
            Body=f.read(),
            Key=f"{int(time.time())}_{FILENAME_SUFFIX}.{FILETYPE}",
        )
        print(response)


if __name__ == "__main__":
    main()
