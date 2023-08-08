#!/usr/bin/python3
"""Function that fetches Reddit API and returns hot article
 titles for a subreddit; returns None if no results."""
import requests

def recurse(subreddit, hot_list=None, after="", count=0):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list

# Example usage
subreddit_name = "python"
result = recurse(subreddit_name)

if result is None:
    print("Invalid subreddit.")
else:
    for idx, title in enumerate(result, start=1):
        print(f"{idx}. {title}")
