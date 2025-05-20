# executor.py
from youtubesearchpython import VideosSearch
import subprocess
import json

with open("apps_config.json") as f:
    APPS = json.load(f)

def open_in_chrome(url):
    chrome_path = APPS.get("chrome")
    if chrome_path:
        subprocess.Popen([chrome_path, url])
    else:
        print("❌ Chrome path not found in apps_config.json.")

def get_first_video_url(query):
    videosSearch = VideosSearch(query, limit=1)
    results = videosSearch.result()
    if results and "result" in results and len(results["result"]) > 0:
        video_id = results["result"][0]["id"]
        return f"https://www.youtube.com/watch?v={video_id}"
    return None

def execute_command(action):
    if action["type"] == "youtube_search":
        url = f"https://www.youtube.com/results?search_query={action['query']}"
        print(f"🦊 Searching YouTube for: {action['query']}")
        open_in_chrome(url)

    elif action["type"] == "youtube_play":
        url = get_first_video_url(action['query'])
        if url:
            print(f"🦊 Playing on YouTube: {action['query']}")
            open_in_chrome(url)
        else:
            print("❌ Could not find video.")

    elif action["type"] == "app":
        app = action["name"]
        if app in APPS:
            print(f"🦊 Opening {app}...")
            subprocess.Popen(APPS[app], shell=True)
        else:
            print(f"❌ I don't know how to open {app} yet.")
    else:
        print("❓ Command not recognized.")
