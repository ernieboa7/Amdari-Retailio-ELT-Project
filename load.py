from dotenv import load_dotenv
load_dotenv()

import os
import boto3

REGION = "eu-north-1"
BUCKET = "retialio-datalake-ernest"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")

datasets = {
    "products": os.path.join(DATA_DIR, "products.csv"),
    "sales":    os.path.join(DATA_DIR, "sales.csv"),
}

s3_client = boto3.client("s3", region_name=REGION)

for name, path in datasets.items():
    if not os.path.exists(path):
        print(f"Missing: {path}")
        continue

    s3_key = f"raw_and_clean/{name}/{name}.csv"  # EXACT filenames Airbyte reads

    with open(path, "rb") as f:
        s3_client.upload_fileobj(f, BUCKET, s3_key)

    print(f" Uploaded -> s3://{BUCKET}/{s3_key}")
