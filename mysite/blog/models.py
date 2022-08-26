from tokenize import blank_re
from django.db import models
from account.models import CustomUser as User
from django.utils import timezone 

#___________________________________________________________________________________________________
#profile

class Profile(models.Model):

    gender_choice=(
        ('female','خانم'),
        ('male', 'آقا')
    ) 

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری')

    image = models.ImageField('تصویر',default='/static/images/profile_pictures/default.png',
                                upload_to="blog/static/images/profile_pictures",
                                blank=True, null=True)

    
    first_name = models.CharField('نام',max_length=50, help_text="Enter your first name")
    last_name = models.CharField('نام خانوادگی',max_length=50, help_text="Enter your last name")
    age = models.IntegerField('سن',help_text="Enter your age")
    gender = models.CharField('جنسیت',max_length=10, choices=gender_choice, null=True, blank=True)
    # phone_number = models.CharField('تلفن همراه',max_length=11)
    address = models.TextField(' آدرس')

    class Meta:
        verbose_name ='پروفایل کاربری'
        verbose_name_plural= 'پروفایل کاربری'

    def __str__(self):
        return self.user.get_full_name()
#___________________________________________________________________________________________________
# post

class Post(models.Model):

    status_choice=(
        ('published','منتشر شده'),
        ('draft', 'Draft')
    )

    title= models.CharField(max_length= 80, verbose_name= 'عنوان')
    slug= models.SlugField(max_length=100, verbose_name= 'slug')
    descripton= models.TextField(verbose_name= 'توضیحات پست')
    created= models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)
    status= models.CharField(max_length=80, choices=status_choice, default='draft', verbose_name= 'وضعیت')
    published= models.DateTimeField(default=timezone.now, verbose_name= 'انتشار پست')
    #------many-to-one relation ba author o post
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    like = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def likes_number(self):
        return self.like.count()


    def __str__(self):
     return self.title


    class Meta:
        # tartibe neshun dadane post az akhar b aval
        ordering = ['-published']
        verbose_name= 'پست'
        verbose_name_plural= 'پست ها'

#___________________________________________________________________________________________________

class Comment(models.Model):

    #------many-to-one post & cm
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    #------many-to-one relation
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_comments')
    content =models.TextField()
    created =models.DateTimeField(auto_now_add= True, )
    
    
    def __str__(self):
        return "{}  : \n {}".format(self.author,self.content)
    
    
    class  Meta:
        ordering = ["-created"]
        verbose_name ='کامنت'
        verbose_name_plural= 'کامنت'

#______________________________________________________________________________________________________
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_like')
    post = models.ForeignKey(Post,on_delete= models.CASCADE, related_name='post_like')

    def __str__ (self):
        return self.post



