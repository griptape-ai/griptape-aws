import boto3

from griptape.structures import Agent
from griptape.aws.tools import AwsIamTool

# Initialize the AWS IAM client
aws_iam_client = AwsIamTool(session=boto3.Session())

# Create an agent with the AWS IAM client tool
agent = Agent(tools=[aws_iam_client])

# Run the agent with a high-level task
agent.run("List all my IAM users")
