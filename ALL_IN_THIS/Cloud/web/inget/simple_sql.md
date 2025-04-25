# inget

打开靶机后要求我们输入id，尝试bypass，是绕过的意思吗？

这样的话我们尝试sql注入，使用 '来试试有没有回显，很明显是没有的

再尝试?id=1' and  '1'='1，结果也没有回显

结合题目猜测要使用万能密码绕过，尝试?id=1' or '1' = '1，得到flag



![image-20250415154450690](C:\Users\曾凯\AppData\Roaming\Typora\typora-user-images\image-20250415154450690.png)