from http.client import responses
from re import search

import requests

from map_filter import mapped_data


def get_url() -> str:
    return "https://dummyjson.com/posts"

def get_data(endpoint: str = "posts") -> list[dict]:
    url = get_url() + endpoint
    params = {"limit": 300 }
    response = requests.get(url, params=params)
    response_json = response.json()
    data = response_json[endpoint]
    return data

def get_usetname() -> str:
    name = input("Username: ")
    return name

def get_user_text():
    word_to_search = ""
    while len(word_to_search.strip()) < 3:
     word_to_search = input("Введіть слово для пошуку в постах: ").strip()
        if len(word_to_search) >= 3:
            return word_to_search

def get_post_bodies(search_text: str, posts_data: list[dict]) -> dict[int, str]:
    for post in posts_data:
        body: str = post["body"].lower()
        if search_text.lower() in body:
           result.append({post["id"]: body})

    result = [{post["id"]: post["body"]}
              for post in posts_data
              if search_text.lower() in post["body"].lower()
    ]
    filtered = filter(lambda post: search_text.lower() in post["body"].lower(), posts_data)
    mapped = map(lambda post: {post["id"]: post["body"])
    return result
    pass


def main():
    name = get_usetname()
    print(f'Hello, {name}')
    search_text = get_user_text()
    data = get_data()
    relevant_data = get_post_bodies(search_text, data)
    for post in relevant_data:
        print(post)


if __name__ == "__main__"
    main()