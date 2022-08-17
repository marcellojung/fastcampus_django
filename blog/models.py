import re
from django.conf import settings
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

REGION_CHOICE = (
    ('Africa', '아프리카'),
    ('Europe', '유럽'),
    ('Oceania', '오세아니아'),
    ('Asia', '아시아'),
    ('North America', '북아메리카'),
    ('South America', '남아메리카'),
)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)  #회원가입만 가능한 사람만 포스트 작성 가능함. 1:N 관계 지정 
    title = models.CharField(max_length=100,verbose_name="제목")
    content = models.TextField(blank=True,verbose_name="내용")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    region = models.CharField(max_length=20,choices=REGION_CHOICE,default='Asia')
    langlat = models.CharField(max_length=50,blank=True,
                               help_text="위경도를 입력해주세요",
                               validators=[lnglat_validator]  #list ㅎ형태 
                               )
    email = models.EmailField()
    tag_set = models.ManyToManyField('Tag')
    
    class Meta:
        ordering = ['updated_at']
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name