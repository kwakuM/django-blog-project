# Create your views here.
from django.http import HttpResponse
def post_search(request,term):
	posts=Post.objects.filter(post_body__contains=str(term))
  	#return HttpResponse(posts)
	t = loader.get_template('blog/post_search.html')
    	c = Context({'posts':posts,'term':term })
    	return HttpResponse(t.render(c))

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Post, Comment 


def post_list(request):
    posts= Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))

    print type(post_list)
    print post_list
    
    return HttpResponse('This should be a list of posts!')

def post_detail(request, id, showComments=False):
	posts=Post.objects.filter(pk=id)
	comments=Comment.objects.filter(comment_post=id)
	"""if showComments==True:
		for post in posts:
			print post
			for comments in comments:
				print comments
			post_comment=post,":",comments
		return  HttpResponse(post_comment)
	else:
		for post in response:
			print post
		return HttpResponse(post)"""
      	t = loader.get_template('blog/post_detail.html')
	c = Context({'posts':posts,'comment':comments})
	return HttpResponse(t.render(c))


def home(request):
    #print 'it works'
    #return HttpResponse('hello world. Ete s3n?') 
     return render_to_response('blog/base.html',{})


