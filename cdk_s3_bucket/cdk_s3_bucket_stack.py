from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy  # Make sure to import RemovalPolicy
)
from constructs import Construct


class CdkS3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creating an S3 Bucket
        s3.Bucket(self, "MyFirstBucket",
                  versioned=True,
                  removal_policy=RemovalPolicy.DESTROY,  # This is now fixed
                  auto_delete_objects=True
                  )
