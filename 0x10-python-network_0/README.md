# Python - Network #0

## HTTP (HyperText Transfer Protocol)

**HTTP (Hypertext Transfer Protocol)** is perhaps the most popular application protocol used in the Internet (or The WEB).

* HTTP is an *asymmetric request-response client-server* protocol.  An HTTP client sends a request message to an HTTP server.  The server, in turn, returns a response message.  In other words, HTTP is a *pull* protocol, the client *pulls* information from the server (instead of server *pushes* information down to the client).

![httpdiagram](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP.png)

**-asymmetric:**  refers to the fact that the roles and responsibilities of the client and server are different in the request-response communication.

* HTTP is a **stateless** protocol. In other words, the current request does not know what has been done in the previous requests.

* HTTP permits negotiating of data type and representation, so as to allow systems to be built independently of the data being transferred.

* Quoting from the RFC2616: "The Hypertext Transfer Protocol (HTTP) is an application-level protocol for distributed, collaborative, hypermedia information systems. It is a generic, stateless, protocol which can be used for many tasks beyond its use for hypertext, such as name servers and distributed object management systems, through extension of its request methods, error codes and headers."

### Browser

Whenever you issue a URL from your browser to get a web resource using HTTP, e.g. ```http://www.nowhere123.com/index.html```, the browser turns the URL into a *request message* and sends it to the HTTP server. The HTTP server interprets the request message, and returns you an appropriate response message, which is either the resource you requested or an error message.

![requestmessage](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_Steps.png)


### HTTP Protocol

The browser translated the URL ```http://www.nowhere123.com/doc/index.html```.

When this request message reaches the server, the server can take either one of these actions:

**1.** The server interprets the request received, maps the request into a **file** under the server's document directory, and returns the file requested to the client.

**2.** The server interprets the request received, maps the request into a **program** kept in the server, executes the program, and returns the output of the program to the client.

**3.** The request cannot be satisfied, the server returns an **error message**.

The browser receives the response message, interprets the message and displays the contents of the message on the browser's window according to the media type of the response (as in the Content-Type response header). Common media type include "text/plain", "text/html", "image/gif", "image/jpeg", "audio/mpeg", "video/mpeg", "application/msword", and "application/pdf".

In its idling state, an HTTP server does nothing but listening to the IP address(es) and port(s) specified in the configuration for incoming request. When a request arrives, the server analyzes the message header, applies rules specified in the configuration, and takes the appropriate action. The webmaster's main control over the action of web server is via the configuration.

### HTTP over TCP/IP

HTTP is a **client-server application-level protocol**. It typically runs over a TCP/IP connection. (HTTP needs not run on TCP/IP. It only presumes a reliable transport. Any transport protocols that provide such guarantees can be used.)

![http-tcp](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_OverTCPIP.png)

**TCP/IP (Transmission Control Protocol/Internet Protocol) is a set of transport and network-layer protocols for machines to communicate with each other over the network.**

**IP (Internet Protocol) is a network-layer protocol, deals with network addressing and routing.**

**TCP (Transmission Control Protocol) is a transport-layer protocol, responsible for establish a connection between two machines.** TCP consists of 2 protocols: TCP and UDP (User Datagram Package).  TCP is reliable, each packet has a sequence number, and an acknowledgement is expected.  A packet will be re-transmitted if it is not received by the receiver.  Packet delivery is guaranteed in TCP.  UDP does not guarantee packet delivery, and is therefore not reliable.  However, UDP has less network overhead and can be used for applications such as video and audio streaming, where reliability is not critical.

**TCP multiplexes applications within an IP machine. For each IP machine, TCP supports (multiplexes) up to 65536 ports (or sockets), from port number 0 to 65535.**  An application, such as HTTP or FTP, runs (or listens) at a particular port number for incoming requests. Port 0 to 1023 are pre-assigned to popular protocols, e.g., HTTP at 80, FTP at 21, Telnet at 23, SMTP at 25, NNTP at 119, and DNS at 53.  Port 1024 and above are available to the users.

Although TCP port 80 is pre-assigned to HTTP, as the default HTTP port number, this does not prohibit you from running an HTTP server at other user-assigned port number (1024-65535) such as 8000, 8080, especially for test server. You could also run multiple HTTP servers in the same machine on different port numbers. When a client issues a URL without explicitly stating the port number, e.g., ```http://www.nowhere123.com/docs/index.html```, the browser will connect to the default port number 80 of the host ```www.nowhere123.com```. You need to explicitly specify the port number in the URL, e.g. ```http://www.nowhere123.com:8000/docs/index.html``` if the server is listening at port 8000 and not the default port 80.

In brief, to communicate over TCP/IP, you need to know (a) IP address or hostname, (b) Port number.

### HTTP Request and Response Messages

HTTP client and server communicate by sending text messages. The client sends a *request* message to the server.  The server, in turn, returns a *response* message.

An HTTP message consists of a **message header and an optional message body, separated by a blank line**.

![httprr](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_MessageFormat.png)

#### HTTP Request Message
---
<br>
The format of an HTTP request message is as follow:

![httprr2](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_RequestMessage.png)

**Request Line**

The first line of the header is called the **request line**, followed by **optional request headers**.

The request line has the following syntax:

```request-method-name request-URI HTTP-version```

* **request-method-name:** HTTP protocol defines a set of request methods, e.g., GET, POST, HEAD, and OPTIONS. The client can use one of these methods to send a request to the server.

* **request-URI:** specifies the resource requested.

* **HTTP-version:** Two versions are currently in use: HTTP/1.0 and HTTP/1.1.

Examples of request line are:

```
GET /test.html HTTP/1.1
HEAD /query.html HTTP/1.0
POST /index.html HTTP/1.1
```

**Request Headers**

The request headers are in the form of **name:value pairs.** Multiple values, separated by commas, can be specified.

```request-header-name: request-header-value1, request-header-value2, ...```

Examples of request headers are:

```
Host: www.xyz.com
Connection: Keep-Alive
Accept: image/gif, image/jpeg, */*
Accept-Language: us-en, fr, cn
```

Example:
The following shows a sample HTTP request message:

![example](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_RequestMessageExample.png)

#### HTTP Request Message
---
<br>
The format of the HTTP response message is as follows:

![format](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_ResponseMessage.png)

**Status Line**

The first line is called the **status line**, followed by **optional response header(s).**

The status line has the following syntax:

```HTTP-version status-code reason-phrase```

* **HTTP-version:** The HTTP version used in this session. Either HTTP/1.0 and HTTP/1.1.

* **status-code:** a 3-digit number generated by the server to reflect the outcome of the request.

* **reason-phrase:** gives a short explanation to the status code.

* Common status code and reason phrase are "200 OK", "404 Not Found", "403 Forbidden", "500 Internal Server Error".

Examples of status line are:

```
HTTP/1.1 200 OK
HTTP/1.0 404 Not Found
HTTP/1.1 403 Forbidden
```

**Response Headers**

The response headers are in the form **name:value pairs**:

```response-header-name: response-header-value1, response-header-value2, ...```

Examples of response headers are:

```
Content-Type: text/html
Content-Length: 35
Connection: Keep-Alive
Keep-Alive: timeout=15, max=100
```

The response message body contains the resource data requested.

Example:
The following shows a sample response message:

![responsemessage](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_ResponseMessageExample.png)

### HTTP Request Methods

HTTP protocol defines a set of request methods. A client can use one of these request methods to send a request message to an HTTP server. The methods are:

* **GET:** A client can use the GET request to get a web resource from the server.

* **HEAD:** A client can use the HEAD request to get the header that a GET request would have obtained. Since the header contains the last-modified date of the data, this can be used to check against the local cache copy.

* **POST:** Used to post data up to the web server.

* **PUT:** Ask the server to store the data.

* **DELETE:** Ask the server to delete the data.

* **TRACE:** Ask the server to return a diagnostic trace of the actions it takes.

* **OPTIONS:** Ask the server to return the list of request methods it supports.

* **CONNECT:** Used to tell a proxy to make a connection to another host and simply reply the content, without attempting to parse or cache it. This is often used to make SSL connection through the proxy.

* Other extension methods.

### "GET" Request Method

```
GET request-URI HTTP-version
(optional request headers)
(blank line)
(optional request body)
```

* The keyword GET is case sensitive and must be in uppercase.

* ***request-URI:*** specifies the path of resource requested, which must begin from the root "/" of the document base directory.

* ***HTTP-version:*** Either HTTP/1.0 or HTTP/1.1. This client negotiates the protocol to be used for the current session. For example, the client may request to use HTTP/1.1. If the server does not support HTTP/1.1, it may inform the client in the response to use HTTP/1.0.

* The client uses the optional request headers (such as Accept, Accept-Language, and etc) to negotiate with the server and ask the server to deliver the preferred contents (e.g., in the language that the client preferred).

* GET request message has an optional request body which contains the query string

#### HTTP/1.0 GET Request
---
<br>
the client issues a GET request to ask for a document named "/index.html"; and negotiates to use HTTP/1.0 protocol. A blank line is needed after the request header. This request message does not contain a body.

The server receives the request message, interprets and maps the request-URI to a document under its document directory. If the requested document is available, the server returns the document with a response status code "200 OK". The response headers provide the necessary description of the document returned, such as the last-modified date (Last-Modified), the MIME type (Content-Type), and the length of the document (Content-Length). The response body contains the requested document. The browser will format and display the document according to its media type (e.g., Plain-text, HTML, JPEG, GIF, and etc.) and other information obtained from the response headers.


**Notes:**

* If the request method name was incorrectly spelt, the server would return an error message "501 Method Not Implemented".

* If the request method name is not allowed, the server will return an error message "405 Method Not Allowed". E.g., DELETE is a valid method name, but may not be allowed (or implemented) by the server.

* If the request-URI does not exist, the server will return an error message "404 Not Found". You have to issue a proper request-URI, beginning from the document root "/". Otherwise, the server would return an error message "400 Bad Request".

* If the HTTP-version is missing or incorrect, the server will return an error message "400 Bad Request".

* In HTTP/1.0, by default, the server closes the TCP connection after the response is delivered. If you use telnet to connect to the server, the message "Connection to host lost" appears immediately after the response body is received. You could use an optional request header "Connection: Keep-Alive" to request for a persistent (or keep-alive) connection, so that another request can be sent through the same TCP connection to achieve better network efficiency. On the other hand, HTTP/1.1 uses keep-alive connection as default.

#### Response Status Code
---
<br>
The first line of the response message (i.e., the status line) contains the response status code, which is generated by the server to indicate the outcome of the request.

The status code is a 3-digit number:

* **1xx (Informational):** Request received, server is continuing the process.
* **2xx (Success):** The request was successfully received, understood, accepted and serviced.
* **3xx (Redirection):** Further action must be taken in order to complete the request.
* **4xx (Client Error):** The request contains bad syntax or cannot be understood.
* **5xx (Server Error):** The server failed to fulfill an apparently valid request.

Some commonly encountered status codes are:

* 100 Continue: The server received the request and in the process of giving the response.

* 200 OK: The request is fulfilled.

* 301 Move Permanently: The resource requested for has been permanently moved to a new location. The URL of the new location is given in the response header called Location. The client should issue a new request to the new location. Application should update all references to this new location.

* 302 Found & Redirect (or Move Temporarily): Same as 301, but the new location is temporarily in nature. The client should issue a new request, but applications need not update the references.

* 304 Not Modified: In response to the If-Modified-Since conditional GET request, the server notifies that the resource requested has not been modified.

* 400 Bad Request: Server could not interpret or understand the request, probably syntax error in the request message.

* 401 Authentication Required: The requested resource is protected, and require client’s credential (username/password). The client should re-submit the request with his credential (username/password).

* 403 Forbidden: Server refuses to supply the resource, regardless of identity of client.

* 404 Not Found: The requested resource cannot be found in the server.

* 405 Method Not Allowed: The request method used, e.g., POST, PUT, DELETE, is a valid method. However, the server does not allow that method for the resource requested.

* 408 Request Timeout

* 414 Request URI too Large

* 500 Internal Server Error: Server is confused, often caused by an error in the server-side program responding to the request.

* 501 Method Not Implemented: The request method used is invalid (could be caused by a typing error, e.g., "GET" misspell as "Get").

* 502 Bad Gateway: Proxy or Gateway indicates that it receives a bad response from the upstream server.

* 503 Service Unavailable: Server cannot response due to overloading or maintenance. The client can try again later.

* 504 Gateway Timeout: Proxy or Gateway indicates that it receives a timeout from an upstream server.

#### HTTP/1.1 GET Request
---
<br>
HTTP/1.1 server supports so-called *virtual hosts*. That is, the same physical server could house several virtual hosts, with different hostnames (e.g., www.nowhere123.com and www.test909.com) and their own dedicated document root directories. Hence, in an HTTP/1.1 GET request, it is mandatory to include a request header called "Host", to select one of the virtual hosts.

#### Conditional GET Requests
---
<br>
You may use additional request header to issue a "conditional request". For example, to ask for the document based on the last-modified date (so as to decide whether to use the local cache copy), or to ask for a portion of the document (or range) instead of the entire document (useful for downloading large documents).

The conditional request headers include:

* ```If-Modified-Since``` (check for response status code "304 Not Modified").

* ```If-Unmodified-Since```

* ```If-Match```

* ```If-None-Match```

* ```If-Range```

#### Request Headers
---
<br>

* **Host: *domain-name*** - HTTP/1.1 supports virtual hosts. Multiple DNS names (e.g., www.nowhere123.com and www.nowhere456.com) can reside on the same physical server, with their own document root directories. Host header is mandatory in HTTP/1.1 to select one of the hosts.

* **Accept: *mime-type-1, mime-type-2, ...*** - The client can use the Accept header to tell the server the MIME types it can handle and it prefers. If the server has multiple versions of the document requested (e.g., an image in GIF and PNG, or a document in TXT and PDF), it can check this header to decide which version to deliver to the client. (E.g., PNG is more advanced more GIF, but not all browser supports PNG.) This process is called content-type negotiation.

* **Accept-Language: *language-1, language-2, ...*** - The client can use the Accept-Language header to tell the server what languages it can handle or it prefers. If the server has multiple versions of the requested document (e.g., in English, Chinese, French), it can check this header to decide which version to return. This process is called language negotiation.

* **Accept-Charset: *Charset-1, Charset-2, ...*** - For character set negotiation, the client can use this header to tell the server which character sets it can handle or it prefers. Examples of character sets are ISO-8859-1, ISO-8859-2, ISO-8859-5, BIG5, UCS2, UCS4, UTF8.

* **Accept-Encoding: *encoding-method-1, encoding-method-2, ...*** - The client can use this header to tell the server the type of encoding it supports. If the server has encoded (or compressed) version of the document requested, it can return an encoded version supported by the client. The server can also choose to encode the document before returning to the client to reduce the transmission time. The server must set the response header "Content-Encoding" to inform the client that the returned document is encoded. The common encoding methods are "x-gzip (.gz, .tgz)" and "x-compress (.Z)".

* **Connection: *Close|Keep-Alive***- The client can use this header to tell the server whether to close the connection after this request, or to keep the connection alive for another request. HTTP/1.1 uses persistent (keep-alive) connection by default. HTTP/1.0 closes the connection by default.

* **Referer: *referer-URL*** - The client can use this header to indicate the referrer of this request. If you click a link from web page 1 to visit web page 2, web page 1 is the referrer for request to web page 2. All major browsers set this header, which can be used to track where the request comes from (for web advertising, or content customization). Nonetheless, this header is not reliable and can be easily spoofed. Note that Referrer is misspelled as "Referer" (unfortunately, you have to follow too).

* **User-Agent: *browser-type*** - Identify the type of browser used to make the request. Server can use this information to return different document depending on the type of browsers.

* **Content-Length: *number-of-bytes*** - Used by POST request, to inform the server the length of the request body.

* **Content-Type: *mime-type*** - Used by POST request, to inform the server the media type of the request body.

* **Cache-Control: *no-cache|...*** - The client can use this header to specify how the pages are to be cached by proxy server. "no-cache" requires proxy to obtain a fresh copy from the original server, even though a local cached copy is available. (HTTP/1.0 server does not recognize "Cache-Control: no-cache". Instead, it uses "Pragma: no-cache". Included both request headers if you are not sure about the server’s version.)

* **Authorization:** Used by the client to supply its credential (username/password) to access protected resources. (This header will be described in later chapter on authentication.)

* **Cookie: *cookie-name-1=cookie-value-1, cookie-name-2=cookie-value-2, ...*** - The client uses this header to return the cookie(s) back to the server, which was set by this server earlier for state management. (This header will be discussed in later chapter on state management.)

* **If-Modified-Since: *date*** - Tell the server to send the page only if it has been modified after the specific date.

#### GET Request for Directory
---
<br>
Suppose that a directory called "testdir" is present in the document base directory "htdocs".

If a client issues a GET request to "/testdir/" (i.e., at the directory).

**1.** The server will return "/testdir/index.html" if the directory contains a "index.html" file.

**2.** Otherwise, the server returns the directory listing, if directory listing is enabled in the server configuration.

**3.** Otherwise, the server returns "404 Page Not Found".


It is interesting to take note that if a client issue a GET request to "/testdir" (without specifying the directory path "/"), the server returns a "301 Move Permanently" with a new "Location" of "/testdir/",

Most of the browser will follow up with another request to "/testdir/". For example, If you issue ```http://127.0.0.1:8000/testdir``` without the trailing "/" from a browser, you could notice that a trailing "/" was added to the address after the response was given. The morale of the story is: you should include the "/" for directory request to save you an additional GET request.

### "HEAD" Request Method

HEAD request is similar to GET request. However, the server returns only the **response header without the response body**, which contains the actual document. HEAD request is useful for checking the headers, such as Last-Modified, Content-Type, Content-Length, before sending a proper GET request to retrieve the document.

The syntax of the HEAD request is as follows:

```
HEAD request-URI HTTP-version
(other optional request headers)
(blank line)
(optional request body)
```

### "OPTIONS" Request Method

A client can use an OPTIONS request method to query the server which request methods are supported. The syntax for OPTIONS request message is:

```
OPTIONS request-URI|* HTTP-version
(other optional headers)
(blank line)
```

"*" can be used in place of a request-URI to indicate that the request does not apply to any particular resource.

Example:

```
OPTIONS http://www.amazon.com/ HTTP/1.1
Host: www.amazon.com
Connection: Close
(blank line)
```
```
HTTP/1.1 200 OK
Date: Fri, 27 Feb 2004 09:42:46 GMT
Content-Length: 0
Connection: close
Server: Stronghold/2.4.2 Apache/1.3.6 C2NetEU/2412 (Unix)
Allow: GET, HEAD, POST, OPTIONS, TRACE
Connection: close
Via: 1.1 xproxy (NetCache NetApp/5.3.1R4D5)
(blank line)
```

All servers that allow GET request will allow HEAD request. Sometimes, HEAD is not listed.

### Submitting HTML Form Data and Query String

In many Internet applications, such as e-commerce and search engine, the clients are required to submit additional information to the server (e.g., the name, address, the search keywords). Based on the data submitted, the server takes an appropriate action and produces a customized response.

The clients are usually presented with a form (produced using HTML <form> tag). Once they fill in the requested data and hit the submit button, the browser packs the form data and submits them to the server, using either a GET request or a POST request.

![htmlform](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTML_SampleForm.png)

Each field has a ***name*** and can take on a specified ***value***. Once the client fills in the fields and hits the submit button, **the browser gathers each of the fields' name and value, packed them into "name=value" pairs, and concatenates all the fields together using "&" as the field separator**. This is known as a ***query string***. It will send the query string to the server as part of the request.

```name1=value1&name2=value2&name3=value3&...```

Special characters are not allowed inside the query string. They must be replaced by a "%" followed by the ASCII code in Hex. E.g., "~" is replaced by "%7E", "#" by "%23" and so on. Since blank is rather common, it can be replaced by either "%20" or "+" (the "+" character must be replaced by "%2B"). This replacement process is called URL-encoding, and the result is a URL-encoded query string. For example, suppose that there are 3 fields inside a form, with name/value of "name=Peter Lee", "address=#123 Happy Ave" and "language=C++", the URL-encoded query string is:

```name=Peter+Lee&address=%23123+Happy+Ave&Language=C%2B%2B```

The query string can be sent to the server using either HTTP GET or POST request method, which is specified in the <form>'s attribute "method".

```<form method="get|post" action="url">```

If GET request method is used, the URL-encoded query string will be appended behind the request-URI after a "?" character, i.e.,

```
GET request-URI?query-string HTTP-version
(other optional request headers)
(blank line)
(optional request body)
```

Using GET request to send the query string has the following drawbacks:

* The amount of data you could append behind request-URI is limited. If this amount exceed a server-specific threshold, the server would return an error "414 Request URI too Large".

* The URL-encoded query string would appear on the address box of the browser.


POST method overcomes these drawbacks. If POST request method is used, the query string will be sent in the **body of the request message**, where the amount is not limited. The request headers Content-Type and Content-Length are used to notify the server the type and the length of the query string. The query string will not appear on the browser’s address box.

### URL and URI

#### URL (Uniform Resource Locator)
---
<br>
A URL (Uniform Resource Locator), defined in RFC 2396, is used to **uniquely identify a resource over the web**. URL has the following syntax:

```protocol://hostname:port/path-and-file-name```

There are 4 parts in a URL:

**1. Protocol:** The application-layer protocol used by the client and server, e.g., HTTP, FTP, and telnet.

**2. Hostname:** The DNS domain name (e.g., ```www.nowhere123.com```) or IP address (e.g., 192.128.1.2) of the server.

**3.Port:** The TCP port number that the server is listening for incoming requests from the clients.

**4.Path-and-file-name:** The name and location of the requested resource, under the server document base directory.

For example, in the URL ```http://www.nowhere123.com/docs/index.html```, the communication protocol is HTTP; the hostname is ```www.nowhere123.com```. The port number was not specified in the URL, and takes on the default number, which is TCP port 80 for HTTP [STD 2]. The path and file name for the resource to be located is "/docs/index.html".

Other examples of URL are:

```
ftp://www.ftp.org/docs/test.txt
mailto:user@test101.com
news:soc.culture.Singapore
telnet://www.nowhere123.com/
```

**Encoded URL**

URL cannot contain special characters. Special characters are encoded, in the form of %xx, where xx is the ASCII hex code. For example, '~' is encoded as %7e; '+' is encoded as %2b. A blank can be encoded as %20 or '+'. The URL after encoding is called **encoded URL**.

#### URI (Uniform Resource Identifier)
---
<br>
URI (Uniform Resource Identifier), defined in RFC3986, is more general than URL, which can even *locate a fragment within a resource*. The URI syntax for HTTP protocol is:

```http://host:port/path?request-parameters#nameAnchor```

* The request parameters, in the form of name=value pairs, are separated from the URL by a '?'. The name=value pairs are separated by a '&'.

* The #nameAnchor identifies a fragment within the HTML document, defined via the anchor tag <a name="anchorName">...</a>.

* URL rewriting for session management, e.g., "...;sessionID=xxxxxx".

#### "POST" Request Method

POST request method is used to "post" additional data up to the server (e.g., submitting HTML form data or uploading a file). Issuing an HTTP URL from the browser always triggers a GET request. To trigger a POST request, you can use an HTML form with attribute method="post" or write your own network program. For submitting HTML form data, POST request is the same as the GET request except that the URL-encoded query string is sent in the request body, rather than appended behind the request-URI.

The POST request takes the following syntax:

```
POST request-URI HTTP-version
Content-Type: mime-type
Content-Length: number-of-bytes
(other optional request headers)
(URL-encoded query string)
```

Request headers Content-Type and Content-Length is necessary in the POST request to inform the server the media type and the length of the request body.

**POST vs GET for Submitting Form Data**

* The amount of data that can be posted is unlimited, as they are kept in the request body, which is often sent to the server in a separate data stream.

* The query string is not shown on the address box of the browser.

Note that although the password is not shown on the browser’s address box, it is transmitted to the server in clear text, and subjected to network sniffing. Hence, sending password using a POST request is absolutely not secure.

### File Upload using multipart/form-data POST Request 

"RFC 1867: Form-based File upload in HTML" specifies how a file can be uploaded to the server using a POST request from an HTML form. A new attribute type="file" was added to the <input> tag of HTML <form> to support file upload. The file-upload POST data is not URL-encoded (in the standard application/x-www-form-urlencoded), but uses a new MIME type of multipart/form-data.

```html
<html>
<head><title>File Upload</title></head>
<body>
  <h2>Upload File</h2>
  <form method="post" enctype="multipart/form-data" action="servlet/UploadServlet">
    Who are you: <input type="text" name="username" /><br />
    Choose the file to upload:
    <input type="file" name="fileID" /><br />
    <input type="submit" value="SEND" />
  </form>
</body>
</html>
```

![fileupload](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTML_FileUploadForm.png)

When the browser encountered an ```<input>``` tag with attribute type="file", it displays a text box and a "browse..." button, to allow user to choose the file to be uploaded.

When the user clicks the submit button, the browser send the form data and the content of the selected file(s). The old encoding type "application/x-www-form-urlencoded" is inefficient for sending binary data and non-ASCII characters. A new media type "multipart/form-data" is used instead.

Each part identifies the input name within the original HTML form, and the content type if the media is known, or as application/octet-stream otherwise.

The original local file name could be supplied as a "filename" parameter, or in the "Content-Disposition: form-data" header.

### Other Request Methods

* **PUT:** Ask the server to store the data.

* **DELETE:** Ask the server to delete the data.

For security consideration, PUT and DELETE are not supported by most of the production server.

Extension methods (also error codes and headers) can be defined to extend the functionality of the HTTP protocol.

### Content Negotiation

HTTP support content negotiation between the client and the server. A client can use additional request headers (such as Accept, Accept-Language, Accept-Charset, Accept-Encoding) to tell the server what it can handle or which content it prefers. If the server possesses multiple versions of the same document in different format, it will return the format that the client prefers. This process is called **content negotiation.**

#### Content-Type Negotiation
---
<br>
The server uses a MIME configuration file (called "conf\mime.types") to map the file extension to a media type, so that it can ascertain the media type of the file by looking at its file extension. For example, file extensions ".htm", ".html" are associated with MIME media type "text/html", file extension of ".jpg", ".jpeg" are associated with "image/jpeg". When a file is returned to the client, the server has to put up a Content-Type response header to inform the client the media type of the data.

For content-type negotiation, suppose that the client requests for a file call "logo" without specifying its type, and sends an header "Accept: image/gif, image/jpeg,...". If the server has 2 formats of the "logo": "logo.gif" and "logo.jpg", and the MIME configuration file have the following entries:

```
image/gif        gif
image/jpeg       jpeg jpg jpe
```

The server will return "logo.gif" to the client, based on the client Accept header, and the MIME type/file mapping. The server will include a "Content-type: image/gif" header in its response.

However, if the server has 3 "logo.*" files, "logo.gif", "logo.html", "logo.jpg", and "Accept: */*" was used:

```Content-Location: logo.html```

The following Apache’s configuration directives are relevant to content-type negotiation:

* The ```TypeConfig``` directive can be used to specify the location of the MIME mapping file:

```TypeConfig conf/mime.types```

* The ```AddType``` directive can be used to include additional MIME type mapping in the configuration file:

```AddType mime-type extension1 [extension2]```

* The ```DefaultType``` directive gives the MIME type of an unknown file extension (in the Content-Type response header)

```DefaultType text/plain```

#### Encoding Negotiation
---
<br>
A client can use the Accept-Encoding header to tell the server the type of encoding it supports. The common encoding schemes are: "x-gzip (.gz, .tgz)" and "x-compress (.Z)".

```Accept-Encoding: encoding-method-1, encoding-method-2, ...```

Similarly, the AddEncoding directive is used to associate the file extension with the an encoding scheme. For example:

```
AddEncoding x-compress  .Z
AddEncoding x-gzip      .gz .tgz
```

### Persistent (or Keep-alive) Connections

In HTTP/1.0, the server closes the TCP connection after delivering the response by default (Connection: Close). That is, each TCP connection services only one request. This is not efficiency as many HTML pages contain hyperlinks (via <a href="url"> tag) to other resources (such as images, scripts – either locally or from a remote server). If you download a page containing 5 inline images, the browser has to establish TCP connection 6 times to the same server.

The client can negotiate with the server and ask the server not to close the connection after delivering the response, so that another request can be sent through the same connection. This is known as persistent connection (or keep-alive connection). Persistent connections greatly enhance the efficiency of the network. For HTTP/1.0, the default connection is non-persistent. To ask for persistent connection, the client must include a request header "Connection: Keep-alive" in the request message to negotiate with the server.

For HTTP/1.1, the default connection is persistent. The client do not have to sent the "Connection: Keep-alive" header. Instead, the client may wish to send the header "Connection: Close" to ask the server to close the connection after delivering the response.

Persistent connection is extremely useful for web pages with many small inline images and other associated data, as all these can be downloaded using the same connection. The benefits for persistent connection are:

* CPU time and resource saving in opening and closing TCP connection in client, proxy, gateways, and the origin server.

* Request can be "pipelined". That is, a client can make several requests without waiting for each response, so as to use the network more efficiently.

* Faster response as no time needed to perform TCP’s connection opening handshaking.

In Apache HTTP server, several configuration directives are related to the persistent connections:

The KeepAlive directive decides whether to support persistent connections. This takes value of either On or Off.

```KeepAlive On|Off```

The MaxKeepAliveRequests directive sets the maximum number of requests that can be sent through a persistent connection. You can set to 0 to allow unlimited number of requests. It is recommended to set to a high number for better performance and network efficiency.

```MaxKeepAliveRequests 200```

The KeepAliveTimeOut directive set the time out in seconds for a persistent connection to wait for the next request.

```KeepAliveTimeout 10```

### Range Download

```
Accept-Ranges: bytes
Transfer-Encoding: chunked
```

### Cache Control

The client can send a request header "Cache-control: no-cache" to tell the proxy to get a fresh copy from the original server, even thought there is a local cached copy. Unfortunately, HTTP/1.0 server does not understand this header, but uses an older request header "Pragma: no-cache". You could include both headers in your request.

```
Pragma: no-cache
Cache-Control: no-cache
```

## HTTP Cookies

An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to a user's web browser. The browser may store the cookie and send it back to the same server with later requests. Typically, an HTTP cookie is used to tell if two requests come from the same browser—keeping a user logged in, for example. It remembers stateful information for the stateless HTTP protocol.

Cookies are mainly used for three purposes:

* **Session management:** Logins, shopping carts, game scores, or anything else the server should remember

* **Personalization:** User preferences, themes, and other settings

* **Tracking:** Recording and analyzing user behavior

Cookies were once used for general client-side storage. While this made sense when they were the only way to store data on the client, modern storage APIs are now recommended. Cookies are sent with every request, so they can worsen performance (especially for mobile data connections).

### Creating cookies

After receiving an HTTP request, a server can send one or more ```Set-Cookie``` headers with the response. The browser usually stores the cookie and sends it with requests made to the same server inside a ```Cookie``` HTTP header. You can specify an expiration date or time period after which the cookie shouldn't be sent. You can also set additional restrictions to a specific domain and path to limit where the cookie is sent.

#### The ```Set-Cookie``` and ```Cookie``` headers
---
<br>
The ```Set-Cookie``` HTTP response header sends cookies from the server to the user agent. A simple cookie is set like this:

```
Set-Cookie: <cookie-name>=<cookie-value>
```

This instructs the server sending headers to tell the client to store a cookie.

Then, with every subsequent request to the server, the browser sends all previously stored cookies back to the server using the ```Cookie``` header.

```
GET /sample_page.html HTTP/2.0
Host: www.example.org
Cookie: yummy_cookie=choco; tasty_cookie=strawberry

```

#### Define the lifetime of a cookie
---
<br>
Cookies can persist for two different periods, depending on the attributes used with the ```Set-Cookie``` header when they were created:

* **Permanent** cookies are deleted at a date specified by the ```Expires``` attribute or after a period prescribed by the ```Max-Age``` attribute.

* **Session cookies** – cookies without a ```Max age``` or ```Expires``` attribute – are deleted when the current session ends. The browser defines when the "current session" ends, and some browsers use session restoring when restarting. This can cause session cookies to last indefinitely.

```
Set-Cookie: id=a3fWa; Expires=Thu, 31 Oct 2021 07:28:00 GMT;
```

**Note:** When you set an ```Expires``` date and time, they're relative to the client the cookie is being set on, not the server.

If your site authenticates users, it should regenerate and resend session cookies, even ones that already exist, whenever a user authenticates. This approach helps prevent session fixation attacks, where a third party can reuse a user's session.

#### Restrict access to cookies
---
<br>
You can ensure that cookies are sent securely and aren't accessed by unintended parties or scripts in one of two ways: with the ```Secure``` attribute and the ```HttpOnly``` attribute.

A cookie with the ```Secure``` attribute is only sent to the server with an encrypted request over the HTTPS protocol. It's never sent with unsecured HTTP (except on localhost), which means man-in-the-middle attackers can't access it easily. Insecure sites (with http: in the URL) can't set cookies with the ```Secure``` attribute. However, don't assume that ```Secure``` prevents all access to sensitive information in cookies. For example, someone with access to the client's hard disk (or JavaScript if the ```HttpOnly``` attribute isn't set) can read and modify the information.

A cookie with the ```HttpOnly``` attribute is inaccessible to the JavaScript ``Document.cookie`` API; it's only sent to the server. For example, cookies that persist in server-side sessions don't need to be available to JavaScript and should have the HttpOnly attribute. This precaution helps mitigate cross-site scripting (XSS) attacks.

```
Set-Cookie: id=a3fWa; Expires=Thu, 21 Oct 2021 07:28:00 GMT; Secure; HttpOnly
```

#### Define where cookies are sent
---
<br>
The ```Domain``` and ```Path``` attributes define the scope of a cookie: what URLs the cookies should be sent to.

The ```Domain``` attribute specifies which server can receive a cookie.

If specified, then cookies are available on the server and its subdomains. For example, if you set ```Domain=mozilla.org```, cookies are available on ```mozilla.org``` and its subdomains like ```developer.mozilla.org```.

If the server does not specify a ```Domain```, the cookies are available on the server but not on its subdomains. Therefore, specifying ```Domain``` is less restrictive than omitting it. However, it can be helpful when subdomains need to share information about a user.

The ```Path``` attribute indicates a URL path that must exist in the requested URL in order to send the ```Cookie``` header. The %x2F ("/") character is considered a directory separator, and subdirectories match as well.

For example, if you set ```Path=/docs```, these request paths match:

* ```/docs```

* ```/docs/```

* ```/docs/Web/```

* ```/docs/Web/HTTP```

But these request paths don't:

* ```/```

* ```/docsets```

* ```/fr/docs```

#### SameSite attribute
---
<br>

The ```SameSite``` attribute lets servers specify whether/when cookies are sent with cross-site requests (where Site is defined by the registrable domain and the scheme: http or https). This provides some protection against cross-site request forgery attacks (CSRF). It takes three possible values: ```Strict```, ```Lax```, and ```None```.

With ```Strict```, the browser only sends the cookie with requests from the cookie's origin site. ```Lax``` is similar, except the browser also sends the cookie when the user navigates to the cookie's origin site (even if the user is coming from a different site). For example, by following a link from an external site. ```None``` specifies that cookies are sent on both originating and cross-site requests, but only in secure contexts (i.e., if ```SameSite=None``` then the ```Secure``` attribute must also be set). If no ```SameSite``` attribute is set, the cookie is treated as ```Lax```.

```
Set-Cookie: mykey=myvalue; SameSite=Strict
```

**Note:** 

* ```SameSite=Lax``` is the new default if ```SameSite``` isn't specified. Previously, cookies were sent for all requests by default.

* Cookies with ```SameSite=None``` must now also specify the ```Secure``` attribute (they require a secure context).

* Cookies from the same domain are no longer considered to be from the same site if sent using a different scheme (http: or https:).

#### Cookie prefixes
---
<br>
Because of the design of the cookie mechanism, a server can't confirm that a cookie was set from a secure origin or even tell where a cookie was originally set.

A vulnerable application on a subdomain can set a cookie with the ```Domain``` attribute, which gives access to that cookie on all other subdomains. This mechanism can be abused in a session fixation attack. See session fixation for primary mitigation methods.

As a defense-in-depth measure, however, you can use cookie prefixes to assert specific facts about the cookie. Two prefixes are available:

* ```__Host-```
If a cookie name has this prefix, it's accepted in a ```Set-Cookie``` header only if it's also marked with the ```Secure``` attribute, was sent from a secure origin, does not include a ```Domain``` attribute, and has the ```Path``` attribute set to ```/```. This way, these cookies can be seen as "domain-locked".

* ```__Secure-```
If a cookie name has this prefix, it's accepted in a ```Set-Cookie``` header only if it's marked with the ```Secure``` attribute and was sent from a secure origin. This is weaker than the ```__Host-``` prefix.

**Note:** On the application server, the web application must check for the full cookie name including the prefix. User agents do not strip the prefix from the cookie before sending it in a request's ```Cookie``` header.

#### JavaScript access using ```Document.cookie```
---
<br>
You can create new cookies via JavaScript using the ```Document.cookie``` property. You can access existing cookies from JavaScript as well if the ```HttpOnly``` flag isn't set.

```
document.cookie = "yummy_cookie=choco";
document.cookie = "tasty_cookie=strawberry";
console.log(document.cookie);
// logs "yummy_cookie=choco; tasty_cookie=strawberry"
```

Cookies created via JavaScript can't include the ```HttpOnly``` flag.

Cookies available to JavaScript can be stolen through XSS.

### Security

**Note:** When you store information in cookies, keep in mind that all cookie values are visible to, and can be changed by, the end user. Depending on the application, you may want to use an opaque identifier that the server looks up, or investigate alternative authentication/confidentiality mechanisms such as JSON Web Tokens.

Ways to mitigate attacks involving cookies:

* Use the ```HttpOnly``` attribute to prevent access to cookie values via JavaScript.

* Cookies that are used for sensitive information (such as indicating authentication) should have a short lifetime, with the ```SameSite``` attribute set to ```Strict``` or ```Lax```. In browsers that support ```SameSite```, this ensures that the authentication cookie isn't sent with cross-site requests. This would make the request effectively unauthenticated to the application server.

### Tracking and privacy

#### Third-party cookies
---
<br>
If the domain and scheme are different, the cookie is not considered to be from the same site, and is referred to as a third-party cookie. While the server hosting a web page sets first-party cookies, the page may contain images or other components stored on servers in other domains (for example, ad banners) that may set third-party cookies. These are mainly used for advertising and tracking across the web.

A third-party server can create a profile of a user's browsing history and habits based on cookies sent to it by the same browser when accessing multiple sites. Firefox, by default, blocks third-party cookies that are known to contain trackers. Third-party cookies (or just tracking cookies) may also be blocked by other browser settings or extensions. Cookie blocking can cause some third-party components (such as social media widgets) not to function as intended.

There are some useful features available for developers who wish to respect user privacy, and minimize third-party tracking:

* Servers can (and should) set the cookie SameSite attribute to specify whether or not third-party cookies may be sent.

* Cookies Having Independent Partitioned State (CHIPS) enables developers to opt-in their cookies to partitioned storage, with a separate cookie jar per top-level site. This enables valid non-tracking uses of third-party cookies to continue working in browsers that do not allow cookies to be used for third-party tracking.

#### Cookie-related regulations
---
<br>
Legislation or regulations that cover the use of cookies include:

* The General Data Privacy Regulation (GDPR) in the European Union

* The ePrivacy Directive in the EU

* The California Consumer Privacy Act

These regulations include requirements such as:

* Notifying users that your site uses cookies.

* Allowing users to opt out of receiving some or all cookies.

* Allowing users to use the bulk of your service without receiving cookies.

There may be other regulations that govern the use of cookies in your locality. The burden is on you to know and comply with these regulations. There are companies that offer "cookie banner" code that helps you comply with these regulations.

### Other ways to store information in the browser

Another approach to storing data in the browser is the Web Storage API. The window.sessionStorage and window.localStorage properties correspond to session and permanent cookies in duration, but have larger storage limits than cookies, and are never sent to a server. More structured and larger amounts of data can be stored using the IndexedDB API, or a library built on it.

There are some techniques designed to recreate cookies after they're deleted. These are known as "zombie" cookies. These techniques violate the principles of user privacy and user control, may violate data privacy regulations, and could expose a website using them to legal liability.
