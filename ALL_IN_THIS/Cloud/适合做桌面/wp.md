 # 工具的使用
 对于图片的处理，我们会的几招（010editor，记事本，看像素块，使用爆破代码来爆破长宽高）都没用，现在该学新方法了

 使用java打开stegsolve，打开方法：使用cmd打开终端，然后输入D:打开D盘，我的java安装在那里，再用   
 cd _java的bin所在位置_   
 打开java的bin，再在终端输入    
java -jar _stegsolve所在位置_  
就可以打开stegsolve了，把题目给的图片拖到java bin的serve里面，然后在stegsolve中打开图片，切换平面到Red Plane1发现一个二维码，使用QE_Research解码后发现十六进制文件，扔进editor，可以发现是