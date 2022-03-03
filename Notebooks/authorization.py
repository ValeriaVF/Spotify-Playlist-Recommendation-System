import tekore as tk
import httpx

trans = httpx.HTTPTransport(retries=3)
client = httpx.Client(timeout=30, transport=trans)
sender = tk.SyncSender(client=client)
def authorize():
 CLIENT_ID = "f002c97d3d4c45bfa5af92b942322ae3"
 CLIENT_SECRET = "7ea247820d95438792697349048b9210"
 app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
 return tk.Spotify(app_token, sender=sender)


#https://towardsdatascience.com/build-your-first-mood-based-music-recommendation-system-in-python-26a427308d96