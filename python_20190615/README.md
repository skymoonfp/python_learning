# python_20190615

python专题学习
===========================


######Python网络爬虫与信息提取（网易公开课）

    1. 20190615开始
    
    2.  第一周 第1单元 requests库简介
            .api的介绍有点儿啰嗦，直接看源码就能很清楚地看到get, head, post, patch, put, delete这六个方法都是通过return request方法实现的
        第一周 第2单元 robots协议
        第一周 第3单元 5个实例
            例1 直接get(url)
            例2 设置浏览器：get(url, headers={'user-agent': 'Mozilla/5.0'})
            例3 搜索引擎：get(url, params={'key': 'keyword'})，其中key是搜索引擎接口标识，例如，百度是'wd'，keyword是我们要搜索的内容
            例4 下载图片：get(url)，将get(url).content（爬取的图片的二进制码）写入文件
            例5 IP归属地查询——有点儿问题
        第二周 第1单元 bs4库BeautifulSoup类基本元素和遍历功能
        第二周 第2单元 信息标记（XML、JSON和YAML）; find_all 
        第二周 第3单元 实例：中国大学排名（综合运用requests库和bs4库）
        第三周 第1单元 正则表达式 
        第三周 第2单元 实例：淘宝商品比价定向爬虫（综合运用requests库和re库）——有点儿问题，自动跳转到登陆页
        第三周 第3单元 实例：股票数据定向爬虫（综合运用requests库、bs4库和re库）
        第四周 第1单元 Scrapy爬虫框架（5+2结构）
        第四周 第2单元 第一个Scrapy实例；yield；Request, Response, Item及Selector
        第四周 第3单元 实例二：股票数据

    3. 20190619结束


######用Python玩转数据（2017）（B站）

    1. 20190615开始
    
    2. 1-5节（P1 - P34）：数据的获取和处理
       6节（P35 - P40）：数据可视化
       7节（P41 - P47）：GUI
          （P48）：综合应用（从雅虎财经获取股票数据；用GUI展示数据；根据数据绘图）
    
    3. P27的matplotlib.finance没有了，mpl_finance还不知道怎么用
    
    4. P47的PyQt4目前是PyQt5了，而且内容还不太一样：像QWidget类位于PyQt5.QtWidgets模块，而不是PyQt5.QtGui模块；部分参数、字段和方法也对不上号
    
    5. 20190616结束
    

######Python教程_600集Python从入门到精通教程（懂中文就能学会）（B站）

    1. 20190616开始

    2. 第1节 操作系统、虚拟机及Linux（Ubuntu版）基础命令（P3 - P41）
       第2节 Linux远程操作命令（P42 - P）
    
    
    
    