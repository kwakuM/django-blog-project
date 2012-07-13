from django.db import models
from django.contrib import admin

# Create your models here.

class Category(models.Model):
	description=models.CharField(max_length=50)
	title=models.CharField(max_length=50)
	def __unicode__(self):
		return self.title

class Author(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	
	def __unicode__(self):
	        return self.name

class Post(models.Model):
	post_title=models.CharField(max_length=50)	
	post_author=models.ForeignKey(Author)
	post_body=models.TextField()
	category=models.ForeignKey(Category)
	post_create_date=models.DateField()
	post_updated_date=models.DateField()
	#post_comments=models.TextField()
	def __unicode__(self):
	        return self.post_title
	def limit_post(self):
		return self.post_body[:50]

class Comment(models.Model):
	comment_date=models.DateField()
	comment_author=models.CharField(max_length=100)
	comment_body=models.TextField()
	comment_post=models.ForeignKey(Post)

	def __unicode__(self):
	        return self.comment_body
	def limit_body(self):
		return self.body[:60]


class Reply(models.Model):
	reply_Date=models.DateField()
	author=models.ForeignKey(Author)
	reply_Body=models.CharField(max_length=150)
	reply_Comment=models.ManyToManyField(Comment)
	
	def __unicode__(self):
	        return self.reply_body

class comment_inline(admin.TabularInline):
	model=Comment



class PostAdmin(admin.ModelAdmin):
	list_display = ('post_title','post_create_date','post_updated_date')
	list_filter = ('post_title','post_body')
	search_fields = ('post_title','post_body')
	ordering = ('post_title','post_body')
	inline=[comment_inline]



class commentAdmin(admin.ModelAdmin):
	inline=[comment_inline]



	        




