import os
import argparse
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    base_url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {"long_url": url}
    response = requests.post(base_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    base_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    payload = {'units': -1}
    response = requests.get(base_url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def check_bitlink(token, bitlink):
    headers = {'Authorization': f'Bearer {token}'}
    base_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(base_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser(description='Shorten link')
    parser.add_argument('link', type=str)
    args = parser.parse_args()
    link = args.link
    parsed_link = urlparse(link)
    new_link = f'{parsed_link.netloc}{parsed_link.path}'
    try:
        if check_bitlink(token, new_link):
            print(count_clicks(token, new_link))
        else:
            print(shorten_link(token, link))
    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema,
            requests.exceptions.HTTPError):
        print('Please input a correct link')


if __name__ == '__main__':
    main()
