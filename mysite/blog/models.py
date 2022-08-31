from django.db import models
from account.models import CustomUser as User
from django.utils import timezone


class Post(models.Model):
    status_choice = (
        ('published', 'منتشر شده'),
        ('draft', 'Draft')
    )

    title = models.CharField(max_length=80, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, verbose_name='slug')
    description = models.TextField(verbose_name='توضیحات پست')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=80, choices=status_choice, default='draft', verbose_name='وضعیت')
    published = models.DateTimeField(default=timezone.now, verbose_name='انتشار پست')
    # ------many-to-one relation ba author o post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='blog/static/images', null=True, blank=True)
    like = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def likes_number(self):
        return self.like.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'


# ___________________________________________________________________________________________________

class Comment(models.Model):
    # ------many-to-one post & cm
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    # ------many-to-one relation
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return "{}  : \n {}".format(self.author.first_name, self.content)

    class Meta:
        ordering = ["-created"]
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت'


# ______________________________________________________________________________________________________
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

    def __str__(self):
        return self.post

# ___________________________________________________________________________________________________
