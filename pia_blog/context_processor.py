from myblog.models import article
from myblog.models import Category


def dates(request):
        dates = article.objects.datetimes('createtime', 'month', order='DESC')
        return {'dates': dates}


def category(request):
    postlist = Category.objects.all()
    return {"category_list": postlist}
