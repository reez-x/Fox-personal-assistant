# command_parser.py
def parse_command(text):
    text = text.lower()

    if "play" in text and "on youtube" in text:
        keyword = text.split("play")[1].replace("on youtube", "").strip()
        return {"type": "youtube_play", "query": keyword}

    elif "open" in text and "youtube" in text:
        keyword = text.split("open")[1].replace("in youtube", "").strip()
        return {"type": "youtube_search", "query": keyword}

    elif "open" in text:
        app_name = text.replace("open", "").strip()
        return {"type": "app", "name": app_name}

    return {"type": "unknown"}
