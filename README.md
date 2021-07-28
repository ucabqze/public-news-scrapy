# public-news-scrapy
舆情新闻网站爬取，已获得每则新闻的网址，需要抽取其中的正文内容。

一、爬取正文
下载项目后需要修改最外层config.py里的内容，包括数据读取路径、数据输出路径等，对于不同的网页结构需针对性修改xpath语句，同一家网站可能有多种网页结构，需要仔细总结，再将xpath语句按序排列。xpath菜鸟教程：https://www.runoob.com/xpath/xpath-syntax.html
添加好config之后，打开运行main.py即可。

二、保存网页
因为许多网页很快就会失效，所以拿到数据之后最好立马将html保存下来，config里已经将其他配置写好，修改数据读取路径和网页储存文件夹路径即可。
需要注意的是读取数据钱需要先在excel里为每一个新闻分配一个独一无二的idx，column name为“本地html文件名”，方便储存的网页可以和excel中的原新闻链接对应上。

