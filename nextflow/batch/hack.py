#!/usr/bin/env python3

"""
Source me, don't run me.
Actually, eval me (like this):

eval $(python3 hack.py)

Works around https://github.com/nextflow-io/nextflow/issues/860
by looking at the value of AWS_PROFILE and 
setting access key and secret key appropriately.

"""
import os

import boto3


def main():
    "do the work"
    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key
    print("export AWS_ACCESS_KEY_ID={}".format(access_key))
    print("export AWS_SECRET_ACCESS_KEY={}".format(secret_key))
    print("export AWS_DEFAULT_REGION=us-west-2")


if __name__ == "__main__":
    main()
