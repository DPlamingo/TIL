from django.db import models
# 수정, 삭제, 생성등 작업한것 자체가
# Migrations(마이그레이션스) 과정이다~
# makemigrations, migrate 명령어는 꼭 외울것!


# Create your models here.
# 클래스 상속
# 테이블 설계도 == 모델 클래스
# 장고가 ID 알아서 만들어줌
# Model이라는 부모 클래스 상속받음.
class Article(models.Model):
    # ()사항은 제약조건
    title = models.CharField(max_length=10) # 최대길이가 10
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)