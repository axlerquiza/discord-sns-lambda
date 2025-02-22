import json
import requests

def lambda_handler(event, context):
    # Discord webhook URL
    discord_webhook_url = "paste_webhook_url_here" # Paste your own webhook url here
    
    # Extract SNS message
    sns_message = event['Records'][0]['Sns']['Message']
    
    # Format message to send to Discord
    payload = {
        "content": sns_message
    }
    
    # Send message to Discord via the webhook
    response = requests.post(discord_webhook_url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 204:
        print("Message sent to Discord successfully")
    else:
        print(f"Failed to send message to Discord, status code: {response.status_code}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message processed successfully')
    }
