from unittest.mock import Mock
from griptape.aws.tools.aws_pricing.tool import AwsPricingTool

class TestAwsPricingTool:
    def test_init(self):
        mock_session = Mock()
        tool = AwsPricingTool(session=mock_session)
        assert tool is not None
