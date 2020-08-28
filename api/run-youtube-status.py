from flask import Flask, Response, render_template
from base64 import b64encode
from dotenv import load_dotenv, find_dotenv
import requests, locale, os, pyyoutube

load_dotenv(find_dotenv())
load_dotenv(find_dotenv())
locale.setlocale(locale.LC_ALL, 'en_US')

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")

YOUTUBE_API = pyyoutube.Api(api_key=YOUTUBE_API_KEY)

app = Flask(__name__, template_folder="components")


def loadImageB64(url):
    response = requests.get(url)
    return b64encode(response.content).decode("ascii")


def getYoutubeInfo():
    CHANNEL_ID = YOUTUBE_API.get_channel_info(channel_id=YOUTUBE_CHANNEL_ID)
    youtubeInfo = CHANNEL_ID.items[0].to_dict()
    youtubeObjects = {
        "channelName": youtubeInfo['snippet']['title'],
        "channelLogo": loadImageB64(youtubeInfo['snippet']['thumbnails']['high']['url']),
        "channelCountry": youtubeInfo['snippet']['country'],
        "channelCountryLogo": loadImageB64("https://i.ibb.co/3W1mQmN/earth.png"),
        "channelViewCounts": locale.format_string('%d', int(youtubeInfo['statistics']['viewCount']), grouping=True),
        "channelViewLogo": loadImageB64("https://i.ibb.co/RyH0NZb/eye-1.png"),
        "channelSubscriberCount": locale.format_string('%d', int(youtubeInfo['statistics']['subscriberCount']),grouping=True),
        "channelVideoCount": locale.format_string('%d', int(youtubeInfo['statistics']['videoCount']), grouping=True),
        "channelVideoLogo": loadImageB64("https://i.ibb.co/zxtRkpp/cloud-upload-2.png"),
        "channelBanner": youtubeInfo['brandingSettings']['image']['bannerImageUrl'],
        "youtubeIcon": loadImageB64("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/YouTube_light_logo_%282017%29.svg/1920px-YouTube_light_logo_%282017%29.svg.png"),
        "verifiedBadge": loadImageB64("https://www.seekpng.com/png/full/132-1323946_features-overview-youtube-verified-check-mark-png.png")
    }

    return render_template("youtubeStatus.html.j2", **youtubeObjects)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    data = getYoutubeInfo()

    response = Response(data, mimetype="image/svg+xml")
    response.headers["Cache-Control"] = "s-maxage=1"

    return response


if __name__ == "__main__":
    app.run(debug=True)
