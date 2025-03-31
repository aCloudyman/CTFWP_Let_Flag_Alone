ctfhub-xss-反射型

知周所众，xss的题一般是打cookie

xssaq.com

开一个项目，调用里面的配置，

然后在第二个url输入框输入当时提交的url（因为是用get请求的，所以payload就在url里面），

就可以让程序自访问，后台收到请求就可以看到cookie