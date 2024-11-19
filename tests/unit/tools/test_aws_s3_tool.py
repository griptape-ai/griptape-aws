from griptape.aws.tools.aws_s3.tool import AwsS3Tool

class TestAwsS3Tool:
    def test_init(self):
        tool = AwsS3Tool()
        assert tool is not None
