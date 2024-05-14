from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent
from gtts import gTTS
import time
from pygame import mixer  # Load the popular external library


# Create the client
client = TikTokLiveClient(unique_id="@peeeermana")


# Listen to an event manually without using async/await
def on_connect(event):
    print("Connected to @{} (Room ID: {})".format(event.unique_id, client.room_id))


# Or, add it manually via "client.add_listener()"
def on_comment(event):
    print("{} -> {}".format(event.user.nickname, event.comment))
    mytext = f"{event.comment}"
    language = 'id'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    mixer.init()
    mixer.music.load('welcome.mp3')
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

client.on(ConnectEvent, on_connect)
client.on(CommentEvent, on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    client.run()
