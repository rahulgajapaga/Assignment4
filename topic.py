import boto3
import configparser

# Load configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# Get topic name and email address from config file
topic_name = config.get('SNS', 'topic_name')
email_address = config.get('SNS', 'email_address')

# Create an SNS client
sns = boto3.client('sns')

# Create a topic
response = sns.create_topic(Name=topic_name)

# Subscribe an email address to the topic
sns.subscribe(TopicArn=response['TopicArn'], Protocol='email', Endpoint=email_address)

# Print the ARN of the newly created topic
print("Topic ARN:", response['TopicArn'])
