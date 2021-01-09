# Bitly url shorterer

You can shorten links and count clicks with my service.
If you write an original link, like https://yandex.ru, you will get a short link.
If you write a short link, you will get counts clicks during all time.

### How to install
To use the service you should:
 1) clone the repo
  2) add .env file with your 'BITLY_TOKEN'
  3) write: 
  ```
python3 main.py link
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).