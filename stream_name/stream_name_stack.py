import os

from aws_cdk import Stack
from aws_cdk import aws_kinesis as kinesis
from aws_cdk import aws_lambda as lambda_
from constructs import Construct


class StreamNameStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stream = kinesis.Stream(self, "example-stream", stream_name="example-stream")
        get_stream_info = lambda_.Function(
            self,
            "get-stream-info",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="get_stream_info.handle",
            code=lambda_.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "get_stream_info")
            ),
            environment={
                "STREAM_NAME": stream.stream_name,
                "STREAM_ARN": stream.stream_arn,
            },
            function_name="get-stream-info",
        )
