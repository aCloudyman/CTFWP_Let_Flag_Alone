---
title: TUCTF_WP
date: 2025-01-27 10:03:27
tags:
- ctf
- writeup
---

# 1.27TUCTF  WP

## Mystery Box            

ida打开看到可疑字符`ReverseMe`，尝试作为密码，运行程序得出flag

```
Welcome to Mystery Box!
1. Play Game
2. Exit
Enter your choice: 1
Enter the secret code to continue: ReverseMe
Congratulations! You've unlocked the secret feature!
Flag: TUCTF{Banana_Socks}
```



## My First Secret            

常规payload：`username=admin' or 1=1--+&password=1`

得到secret

卡了半天，最后选择去寻找常见的小说电视剧文字，发现是mistborn的（有机会想去看看），让队友找下对应“字典”，结果就出了，感谢唐哥&杰哥！

## Shopping Time            

哈希碰撞

```
import hashlib

target_prefix = "c583600"  # 目标前7位

# 生成MD5哈希值的函数
def generate_md5(input_str):
    return hashlib.md5(input_str.encode()).hexdigest()

# 暴力破解 - 这里只是一个示例，您可以扩展字符集和范围
counter = 0
while True:
    # 生成一个输入字符串（这里是数字，您可以根据需要调整）
    candidate = str(counter)
    
    # 计算该字符串的MD5值
    md5_hash = generate_md5(candidate)
    
    # 检查哈希值的前7位是否匹配
    if md5_hash.startswith(target_prefix):
        print(f"找到匹配的输入: {candidate}")
        print(f"对应的MD5哈希: {md5_hash}")
        break
    
    counter += 1

```

得到输出

```
找到匹配的输入: 74868389
对应的MD5哈希: c583600cce08a9cef93922000e3d1611
```

传入参数即可

## Med Graph            



```
{
  "query": "\nquery {\n    __schema {\n        types {\n            name\n            fields {\n                name\n            }\n        }\n    }\n}\n"
}
```

返回

```
HTTP/2 200 OK
Date: Sun, 26 Jan 2025 17:50:55 GMT
Content-Type: application/json
Content-Length: 5652
Strict-Transport-Security: max-age=0; includeSubDomains

{
  "data": {
    "__schema": {
      "types": [
        {
          "fields": [
            {
              "name": "patient"
            },
            {
              "name": "userData"
            },
            {
              "name": "doctor"
            },
            {
  .........................................
        }
      ]
    }
  }
}

```



## Mystery Presentation

随波逐流一把梭

binwalk之后开俩压缩包就出了

## Packet Detective            

随波逐流直接出`CTF{N3tw0rk_M4st3r}`

## My First Encryption            

xor爆破，

```
def xor_file(input_file, output_file, key):
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        byte = f_in.read(1)
        while byte:
            xor_byte = bytes([byte[0] ^ key])
            f_out.write(xor_byte)
            byte = f_in.read(1)

def brute_force_xor(input_file, output_file):
    # 暴力破解，尝试所有可能的异或密钥
    for key in range(256):  # 256个可能的密钥
        temp_output = 'temp_output.jpg'  # 暂时保存解密后的文件
        xor_file(input_file, temp_output, key)
        
        # 检查文件头是否是FFD8FF
        with open(temp_output, 'rb') as f:
            header = f.read(3)  # 读取文件的前3个字节
            if header == b'\xFF\xD8\xFF':  # 判断是否为JPEG文件头
                print(f"破解成功，找到的密钥是: {key}")
                # 将恢复的内容保存到最终输出文件
                xor_file(input_file, output_file, key)
                return key
    print("没有找到合适的密钥。")
    return None

# 使用示例
input_file = 'flag.jpeg'  # 加密文件路径
output_file = 'decrypted.jpg'  # 解密后的输出文件路径

brute_force_xor(input_file, output_file)

```

发现密钥是48，然后图片也出来了

