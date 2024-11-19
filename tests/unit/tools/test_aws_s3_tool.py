from unittest.mock import Mock
from griptape.aws.tools.aws_s3.tool import AwsS3Tool

class TestAwsS3Tool:
    def test_init(self):
        mock_session = Mock()
        tool = AwsS3Tool(session=mock_session)
        assert tool is not None
        assert tool.session == mock_session
