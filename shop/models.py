from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Shop(models.Model):

    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    explain = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Review(models.Model):
# 관련 Shop
# 리뷰쓴 유저
# 남긴 말 필드
# 인증샷 필드 : 옵션 필드
# 생성일시
# 수정일시
    pass

