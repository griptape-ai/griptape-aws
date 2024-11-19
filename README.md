# Griptape AWS Extension

## Overview
This extension provides several [Tools](https://docs.griptape.ai/stable/griptape-tools/) for [AWS](https://aws.amazon.com/).

```python
import boto3

from griptape.structures import Agent
from griptape.aws.tools import AwsS3Tool

# Initialize the AWS S3 client
aws_s3_client = AwsS3Tool(session=boto3.Session(), off_prompt=True)

# Create an agent with the AWS S3 client tool
agent = Agent(tools=[aws_s3_client])

# Task to list all the AWS S3 buckets
agent.run("List all my S3 buckets.")
```

## Installation

Poetry:
```bash
poetry add https://github.com/griptape-ai/griptape-aws.git
```

Pip:
```bash
pip install git+https://github.com/griptape-ai/griptape-aws.git
```
