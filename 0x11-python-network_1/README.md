# Python - Network #1

Let's try a different approach because the current one is kinda... *time-consuming*. im going to read the resources and all I'm gonna include here is the questions in the general section and their answers as per the resources.

### How to fetch internet resources with the Python package ```urllib```?

The simplest way:

```python
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
```

If you wish to retrieve a resource via URL and store it in a temporary location, you can do so via the ```shutil.copyfileobj()``` and ```tempfile.NamedTemporaryFile()``` functions:

```python
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass
```

Many uses of urllib will be that simple (note that instead of an ‘http:’ URL we could have used a URL starting with ‘ftp:’, ‘file:’, etc.).

HTTP is based on requests and responses - the client makes requests and servers send responses. ```urllib.request``` mirrors this with a Request object which represents the HTTP request you are making. In its simplest form you create a ```Request``` object that specifies the URL you want to fetch. Calling ```urlopen``` with this ```Request``` object returns a response object for the URL requested. This response is a **file-like** object, which means you can for example call ```.read()``` on the response:

```python
import urllib.request

req = urllib.request.Request('http://python.org/')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

Note that ```urllib.request``` makes use of the same ```Request``` interface to handle all URL schemes. For example, you can make an FTP request like so:

```python
req = urllib.request.Request('ftp://example.com/')
```

### How to decode ```urllib``` body response?

First, the encoding:

```python
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```

In Python 3+, You can URL decode any string using the ```unquote()``` function provided by ```urllib.parse``` package. The ```unquote()``` function uses UTF-8 encoding by default.

```python
>>> import urllib.parse
>>> encodedStr = 'Hell%C3%B6%20W%C3%B6rld%40Python'
>>> urllib.parse.unquote(encodedStr)
'Hellö Wörld@Python'
```

**Decoding plus sign (+) to space character**
The ```unquote()``` function does not decode plus sign (```+```)

```python
>>> urllib.parse.unquote('My+name+is+Rajeev')
'My+name+is+Rahaf'
```

But if you’re working with HTML forms then you’ll need to replace plus sign (```+```) with space character because HTML forms use ```application/x-www-form-urlencoded``` MIME type which encodes space character to plus sign (```+```) instead of ```%20```.

For replacing plus sign with space, you can use the ```unquote_plus()``` function of ```urllib.parse``` package 

```python
>>> import urllib.parse
>>> encodedStr = 'My+name+is+Rajeev'
>>> urllib.parse.unquote_plus(encodedStr)
'My name is Rahaf'
```

**URL Decoding multiple query strings at once**

If you want to decode or parse multiple query strings of type ```application/x-www-form-urlencoded``` (e.g ```'name=Rajeev+Singh&phone=%2B919999999999'```), then you can use ```parse_qs``` or ```parse_qsl``` functions provided by ```urllib.parse``` package.

**The ```parse_qs``` function returns a dictionary of key-value pairs whereas the ```parse_qsl``` function returns a list of (key, value) tuples.**

**parse_qs**

```python
>>> import urllib.parse
>>> queryStr = 'name=Rahaf&phone=%2B12345679&phone=%2B12345679'
>>> urllib.parse.parse_qs(queryStr)
{'name': ['Rahaf'], 'phone': ['+123456789', '+12345679']}
```

**parse_qsl**

```python
>>> import urllib.parse
>>> queryStr = 'name=Rahaf&phone=%2B12345679&phone=%2B12345679'
>>> urllib.parse.parse_qsl(queryStr)
[('name', 'Rahaf'), ('phone', '+12345679'), ('phone', '+12345679')]
```

### How to use the Python package ```requests```?

Simply speaking:

```python
>>> import requests
>>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
```

### How to make HTTP GET request?

```python
import requests
r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
```

### How to make HTTP POST/PUT/etc. request?

**POST**

```python
r = requests.post(url=url, data=body)
```

**DELETE**
```python
r = requests.delete(url=url, auth=auth)
```

**HEAD**
```python
r = requests.head(url=url, auth=auth)
```

### How to fetch JSON resources?

There’s also a builtin JSON decoder, in case you’re dealing with JSON data:

```python
import requests

r = requests.get('https://api.github.com/events')
r.json()
[{'repository': {'open_issues': 0, 'url': 'https://github.com/...
```

In case the JSON decoding fails, ```r.json()``` raises an exception. For example, if the response gets a 204 (No Content), or if the response contains invalid JSON, attempting ```r.json()``` raises ```requests.exceptions.JSONDecodeError```. This wrapper exception provides interoperability for multiple exceptions that may be thrown by different python versions and json serialization libraries.

It should be noted that **the success of the call to ```r.json()``` does not indicate the success of the response**. Some servers may return a JSON object in a failed response (e.g. error details with HTTP 500). Such JSON will be decoded and returned. **To check that a request is successful, use ```r.raise_for_status()``` or check ```r.status_code``` is what you expect.**

### How to manipulate data from an external service?
