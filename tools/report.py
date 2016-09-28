"""Ingress report utils"""
from utils.functions import command
from urllib.parse import urlsplit
import urllib
import urllib.request
import xml.etree.ElementTree as ET


YT_ANNOTATIONS_SERVICE = "https://www.youtube.com/annotations_invideo?features=1&legacy=1&video_id="


@command("report", store=False)
def ingress_report(link):
    """Text annotations from Ingress Report YT video (first /new <yt-link>)"""
    # Validate link
    parsed = urllib.parse.urlparse(link)
    if parsed.scheme != 'https' or (parsed.netloc != 'youtu.be' and parsed.netloc != 'www.youtube.com'):
        return link

    if parsed.netloc == 'youtu.be':
        video_id = parsed.path[1:]
    elif parsed.netloc == 'www.youtube.com':
        video_id = urllib.parse.parse_qs(parsed.query).get('v')
        if video_id is None or len(video_id) > 1:
            return link
        video_id = video_id[0]
    else:
        return link

    xml = urllib.request.urlopen(YT_ANNOTATIONS_SERVICE + video_id).read()
    return [t.text for t in ET.fromstring(xml).iter('TEXT') if t.text not in ['Subscribe', 'Android', 'iOS', 'https://play.google.com/store/apps/details?id=com.nianticproject.ingress']]
