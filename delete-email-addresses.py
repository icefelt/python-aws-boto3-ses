import boto3

# Create SES client
ses = boto3.client('ses')

response = ses.delete_identity(
  Identity = 'EMAIL_ADDRESS'
)

print(response)