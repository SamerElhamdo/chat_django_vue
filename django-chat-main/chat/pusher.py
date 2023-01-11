import imp
from .secrets import SECRET
import pusher

pusher_client = pusher.Pusher(
    app_id = "1536673",
    key = "9e12adb124b797089b79",
    secret =  SECRET ,
    cluster = "us2",
    ssl=True
)
