from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
# # 가게명 필드
#     title = models.CharField(max_length=100)
#     phonenumber = CharField(max_length=100)
#     address = models.CharField()
#     explain = models.TextField()
#     photo = models.ImageField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    pass

class Review(models.Model):
# 관련 Shop
# 리뷰쓴 유저
# 남긴 말 필드
# 인증샷 필드 : 옵션 필드
# 생성일시
# 수정일시
    pass

