from griptape.aws.tools.aws_iam.tool import AwsIamTool

class TestAwsIamTool:
    def test_init(self):
        tool = AwsIamTool()
        assert tool is not None
