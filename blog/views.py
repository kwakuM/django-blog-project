# Create your views here.
from django.http import HttpResponse
def views.post_search(request,author):
	response="Written by" + str(author)
	return HttpResponse(response)

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse('This should be a list of posts!')

def post_detail(request, id, showComments=False):
    pass
    
def post_search(request, term):
    pass

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete s3n?') 

