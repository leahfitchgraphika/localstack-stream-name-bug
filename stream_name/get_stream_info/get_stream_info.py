import os


def handle(event, context):
    return {
        "STREAM_NAME": os.environ["STREAM_NAME"],
        "STREAM_ARN": os.environ["STREAM_ARN"],
    }
