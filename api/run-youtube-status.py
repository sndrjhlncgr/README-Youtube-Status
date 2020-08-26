from base64 import b64encode

import requests
from flask import Flask, render_template, Response
from dotenv import load_dotenv, find_dotenv

from pyyoutube import Api

load_dotenv(find_dotenv())

YOUTUBE_API = Api(api_key='AIzaSyABfEd-GTQ1Aff4qye6WqI54_vYv5aqJtw')

app = Flask(__name__, template_folder="components")


def loadImageB64(url):
    response = requests.get(url)
    return b64encode(response.content).decode("ascii")


def getYoutubeInfo():
    CHANNEL_ID = YOUTUBE_API.get_channel_info(channel_id="UCi3mbICnce7yIU1NGhgoSPw")
    youtubeInfo = CHANNEL_ID.items[0]
    youtubeObjects = {
        "channelName": youtubeInfo.snippet.title,
        "channelLogo": loadImageB64(youtubeInfo.snippet.thumbnails.high.url),
        "channelCountry": youtubeInfo.snippet.country,
        "channelViewCounts": youtubeInfo.statistics.viewCount,
        "channelSubscriberCount": youtubeInfo.statistics.subscriberCount,
        "channelVideoCount": youtubeInfo.statistics.videoCount,
        "channelBanner": loadImageB64(youtubeInfo.brandingSettings.image.bannerMobileImageUrl),
        "youtubeIcon": loadImageB64(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/YouTube_light_logo_%282017%29.svg/1920px-YouTube_light_logo_%282017%29.svg.png")
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
