from azure.communication.email import EmailClient
from django.conf import settings


def send_email(subject, to, body):
    email_client = EmailClient.from_connection_string(settings.AZURE_COMMUNICATIONS_CONNECTION_STRING)
    message = {
        "content": {
            "subject": subject,
            "plainText": "Hey! This is a test email. from Azure Communication Services by Adib the Noob",
            "html": body
        },
        "recipients": {
            "to": [
                {
                    "address": to,
                    "displayName": "Test Display Name"
                }
            ]
        },
        "senderAddress": "adib-the-azure-guy@5c205690-56b0-475b-ac15-b3c59cf37e55.azurecomm.net",
    }
    email_client.begin_send(message)
