import os
import sys

# aggiunge src/ al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# dice a Django quale settings usare
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()
async_to_sync(channel_layer.group_send)(
    "accounts",  # nome del gruppo a cui inviare il messaggio
    {
        "type": "send_message",  # metodo del consumer
        "message": "Test notification from script!"
    }
)

print("Notification sent!")