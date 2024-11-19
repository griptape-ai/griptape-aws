from griptape.aws.tools.aws_pricing.tool import AwsPricingTool

class TestAwsPricingTool:
    def test_init(self):
        tool = AwsPricingTool()
        assert tool is not None
