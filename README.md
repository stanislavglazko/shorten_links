# Bitly url shortener

You can shorten links and count clicks with my service.
If you write an original link, like https://yandex.ru, you will get a short link.
If you write a short link, you will get counts clicks during all time.

### How to install
Python3 should be already installed.

To use the service you should:
1) clone the repo
2) use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
    ```
    pip install -r requirements.txt
    ```
3) add .env file in the directory of the service with your `BITLY_TOKEN`:
    ```
    BITLY_TOKEN=<your_bitly_token>
    ```
4) write: 
    ```
    python3 main.py <your_link>
    ```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).