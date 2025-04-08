import requests

SENDGRID_API_KEY = "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"
API_URL = "https://api.sendgrid.com/v3/mail/send"

headers = {
    "Authorization": f"Bearer {SENDGRID_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "personalizations": [
        {
            "to": [
                {"email": "praveenr@xminds.com"}
            ],
            "subject": "SendGrid Test Email"
        }
    ],
    "from": {
        "email": "noreply@x-minds.org"
    },
    "content": [
        {
            "type": "text/plain",
            "value": "Hello Praveen,\n\nThis is a test email sent via SendGrid API.\n\nCheers,\nSendGrid Test Script"
        }
    ]
}

response = requests.post(API_URL, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json() if response.status_code != 202 else "Email sent successfully.")

