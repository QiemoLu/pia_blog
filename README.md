# pia_blog
一个基于django的博客系统，仅实现发表文章和根据条件查询等简单功能  
模板套用自基于https://startbootstrap.com/template-overviews/blog-post/
测试访问地址 http://45.62.119.70
## 依赖
python3  
django1.10  
建议使用virtualenv  
## 如何使用
```
pip install -r requirements.txt 
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 80 # 亦可以使用nginx+uwsgi方式部署
```
## 已实现
支持markdown显示，代码高亮（代码高亮引入highlight.js插件）  
多说评论(请在templates/comment.html中替换short_name为你的多说ID)  
根据标签进行分类显示  
根据发表时间进行归档(精确到月份)  
搜索文章功能(仅支持搜索标题,可自行添加要搜索的区域)  
分页功能(paginator模块)  
文章独立页面和摘要显示  

## 参考文献
(django搭建简易博客教程)  
http://wiki.jikexueyuan.com/project/django-set-up-blog/  
(django学习小组：博客开发实战)  
http://www.jianshu.com/p/3bf9fb2a7e31  
(the django book)  
(django官方文档)
http://python.usyiyi.cn/django/index.html
