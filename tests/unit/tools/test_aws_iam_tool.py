from unittest.mock import Mock
from griptape.aws.tools.aws_iam.tool import AwsIamTool

class TestAwsIamTool:
    def test_init(self):
        mock_session = Mock()
        tool = AwsIamTool(session=mock_session)
        assert tool is not None
