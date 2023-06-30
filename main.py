import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse


def is_bitlink(token, link):
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(api_url, headers=headers)
    return response.ok


def shorten_link(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    payload = {
        'long_url': url
    }

    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()

    shorten_link = response.json()
    bitlink = shorten_link['id']

    return bitlink


def count_clicks(token, bitlink):
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()

    clicks_data = response.json()
    clicks_count = clicks_data['total_clicks']

    return clicks_count


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser(description='сокращает URL')
    parser.add_argument('url', help='URL сократить или Bitlink чтобы получить количесво кликов')
    args = parser.parse_args()
    user_input = args.url

    try:
        if is_bitlink(token, user_input):
            parsed = urlparse(user_input)
            input_url = parsed.netloc if parsed.netloc else parsed.path
            clicks = count_clicks(token, input_url)
            print('Количество кликов:', clicks)
        else:
            parsed = urlparse(user_input)
            input_url = parsed.netloc if parsed.netloc else parsed.path
            if parsed.scheme:
                url_for_short = user_input
            else:
                url_for_short = 'https://' + input_url
            bitlink = shorten_link(token, url_for_short)
            print('Битлинк:', bitlink)

    except requests.exceptions.HTTPError:
        print('Ошибка: Убедитесь, что ввели адрес корректно')

