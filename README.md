### basic setup
```
# create a virtualenv with python 3.6+
virtualenv venv

# install dependencies
pip install -r requirements.txt

# run the script
./run.sh
```

### working example (request_id visible in logs)
```
curl -H "X-Request-Id: heyivica" localhost:5000/working

# and the request_id is shown in the logs
2020-01-23 17:41:43,678 - werkzeug - INFO - request_id=heyivica - 127.0.0.1 - - [23/Jan/2020 17:41:43] "GET /working HTTP/1.1" 500 -

# so is the nasty exception
... SNIP ...
File "/usr/lib/python3.8/json/encoder.py", line 405, in _iterencode_dict
yield from chunks
File "/usr/lib/python3.8/json/encoder.py", line 438, in _iterencode
o = _default(o)
File "/usr/lib/python3.8/json/encoder.py", line 179, in default
raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type EnvironHeaders is not JSON serializable
```

### non-working example (request_id not visible in logs)
```
curl -H "X-Request-Id: heyivica" localhost:5000/notworking

# and the logs
2020-01-23 17:42:17,701 - werkzeug - INFO - request_id=None - 127.0.0.1 - - [23/Jan/2020 17:42:17] "GET /notworking HTTP/1.1" 200 -

# but there is no exception this time and the response shows
{
    "status": "headers",
    "message": [
        [
            "Host",
            "localhost:5000"
        ],
        [
            "User-Agent",
            "curl/7.67.0"
        ],
        [
            "Accept",
            "*/*"
        ],
        [
            "X-Request-Id",
            "heyivica"
        ]
    ]
}

```
