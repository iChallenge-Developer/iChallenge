from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django import forms
# Create your models here.
from django.core.exceptions import ValidationError

def is_ToS(value):
    if value == False:
        raise forms.ValidationError("약관에 동의해야 합니다.")

def nickname_unique(value):
    # social 회원가입 시, 자동으로 nickname에 빈 str이 들어감. 이를 사용자가 변경하지 않을 경우, 다른 사용자가 social 회원가입을 못함.
    # 따라서 User 모델의 nickname field에 unique=True를 주는 것보다, 다음과 같이 처리하는 것이 적절함.
    if value != "":
        if User.objects.filter(nickname=value).exists():
            raise forms.ValidationError("사용자의 닉네임은 이미 존재합니다.")
 
class User(AbstractUser):
    nickname = models.CharField(max_length=100, validators=[nickname_unique], verbose_name="닉네임")
    email = models.EmailField(max_length=255, unique=True, verbose_name="이메일 (ID)")
    username = models.CharField(max_length=150, verbose_name="이름")
    image = models.ImageField(upload_to="profile_photo/%Y/%m/%d/", default="profile_photo/default/DOWITH.png", verbose_name="프로필 사진")
    is_social = models.BooleanField(default=False, verbose_name="소셜 계정")
    is_ToS = models.BooleanField(default=False, validators=[is_ToS], verbose_name="약관 동의")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "nickname"]

    def __str__(self):
        return str(self.nickname)

    # # def clean_fields(self, *args, **kwargs):
    # #     username = self.username
    # #     nickname = self.nickname
    # #     print(username)
    # #     if username == nickname:
    # #         raise ValidationError("둘이 같으면 안돼")
    # #     return super(User, self).clean_fields(*args, **kwargs)
    
    # # def clean_fields(self, *args, **kwargs):
    # #     if self.is_ToS == False:
    # #         raise ValidationError("안돼안돼")
    # #     return super(User, self).clean_fields(*args, **kwargs)
    
    # def clean(self, *args, **kwargs):
    #     if self.is_ToS == False:
    #         raise ValidationError("안돼안돼")
    #     return super(User, self).clean(*args, **kwargs)

    # def clean(self, *args, **kwargs):
    #     if self.username == self.nickname and self.is_ToS == False:
    #         raise ValidationError("둘이 같으면 안돼 / 안돼안돼")
    #     elif self.username == self.nickname:
    #         raise ValidationError("둘이 같으면 안돼")
    #     elif self.is_ToS == False:
    #         raise ValidationError("안돼안돼")
    #     return super(User, self).clean(*args, **kwargs)
    

    # # def clean_is_ToS(self, *args, **kwargs):
    # #     is_ToS = self.cleaned_data.get("is_ToS")
    # #     print(is_ToS)
    # #     if is_ToS == False:
    # #         raise forms.ValidationError("약관에 동의해야 합니다.")
    # #     return is_ToS