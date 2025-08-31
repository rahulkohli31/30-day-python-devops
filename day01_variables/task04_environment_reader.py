import os

aws_region = os.environ.get('AWS_REGION', 'us-east-1a')
debug_mode = os.environ.get('DEBUG', 'false').lower() == 'true'
app_port = int(os.environ.get('PORT', '8080'))

print(f"Region: {aws_region}")
print(f"Debug: {debug_mode}")
print(f"Port: {app_port}")