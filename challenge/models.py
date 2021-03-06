from django.db import models
from django import forms
from login.models import User
import datetime
from hashid_field import HashidField, HashidAutoField

from django.core.exceptions import ValidationError

# User
# - is staff : 내부자냐 아니냐

# Challenge
# - HostUser : user_id
# - is_published : Boolean
# - link_url : /challenge/cr23ou89hnacefijlnsho
# python hash
# URLSAFE : 띄어쓰기, 덧셈이 urlsafe functionå


# def less_then_min_validator(value1, value2):
#     if len(value1) < value2:
#         raise forms.ValidationError("최소 인원보다 작은 수의 인원을 입력하셨습니다.")

def redirect_link(link):
    challenges = Challenge.objects.filter(link=link)
    if len(challenges) == 0:
        return
    else:
        pass
    return

# User <-> Challenge
# --> Enrollment
#      - user_id (User)
#      - challenge_id (Challenge)
#      - result/success
#      - day

# 이미지 저장
# 1. 파일 : Django File Upload
# 2. 외부 클라우드 스토리지 : 서버에서는 사진을 클라우드로 올리고, 클라우드 링크만 갖고있어요
# AWS S3, Microsoft, etc.


class Challenge(models.Model):
    CATEGORY_LANGUAGE = 'language'
    CATEGORY_JOB = 'job'
    CATEGORY_NCS = 'NCS'
    CATEGORY_PROGRAMMING = 'programming'
    CATEGORY_CERTIFICATE = 'certificate'
    CATEGORY_OTHER = 'other'

    CATEGORY_OF_CHALLENGE = (
        (CATEGORY_LANGUAGE, '어학'),
        (CATEGORY_JOB, '취업'),
        (CATEGORY_NCS, '고시/공무원'),
        (CATEGORY_PROGRAMMING, '프로그래밍'),
        (CATEGORY_CERTIFICATE, '자격증'),
        (CATEGORY_OTHER, '기타')
    )

    PRIVATE_OF_CHALLENGE = (
        (0, '전체 공개'),
        (1, '친구 공개'),
        (2, '나만 보기'),
    )

    STATUS_OF_CHALLENGE = (
        (0, '대기 중'),
        (1, '진행 중'),
        (2, '완료'),
    )
    
    id = HashidAutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="제목")
    desc = models.TextField(verbose_name="설명")
    category = models.CharField(
        max_length=100, choices=CATEGORY_OF_CHALLENGE, verbose_name="분류")
    private = models.IntegerField(
        choices=PRIVATE_OF_CHALLENGE, verbose_name="공개 상태")
    status = models.IntegerField(
        choices=STATUS_OF_CHALLENGE, blank=True, null=True, verbose_name="진행 상태")
    min_pp = models.PositiveIntegerField(verbose_name="최소 인원")
    max_pp = models.PositiveIntegerField(verbose_name="최대 인원")
    cur_pp = models.IntegerField(default=0, blank=True)
    start_date = models.DateField(verbose_name="시작일", default=datetime.date.today)
    end_date = models.DateField(verbose_name="종료일")
    created_date = models.DateField(auto_now_add=True, verbose_name="생성일")
    invitation_key = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

#TODO 챌린지 바꾸기
    #def clean(self, *args, **kwargs):
    #    error_list = []
    #    if self.min_pp > self.max_pp:
    #        error_list.append("최대 인원이 최소 인원보다 작을 수 없습니다.")
    #    if self.start_date > self.end_date:
    #        error_list.append("종료일이 시작일보다 빠를 수 없습니다.")
        if self.min_pp == 0:
            error_list.append("최소 인원은 0이 될 수 없습니다.")
        if self.start_date < datetime.date.today():
            error_list.append(f"시작일은 {datetime.date.today()} (오늘) 이전이 될 수 없습니다.")

        
        if len(error_list) > 0:
            raise ValidationError(error_list)

        # return super(User, self).clean(*args, **kwargs)


class Enrollment(models.Model):
    # player_total = 0
    challenge = models.ForeignKey(
        Challenge, on_delete=models.CASCADE, verbose_name="챌린지", related_name="chEnrollment_set")
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="유저", related_name="chEnrollment_set")
    result = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('challenge', 'player',)

    def __str__(self):
        return '{1} : {0}'.format(self.challenge.title, self.player.nickname)

class EnrollmentDate(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name="인롤먼트", related_name="chEnrollmentDate_set")
    date_result = models.BooleanField(default=False)
    date = models.DateField(blank=True) #12시 1분쯤 생성된 시간이 들어감

    def __str__(self):
        return str(self.enrollment.challenge.title) +' '+str(self.enrollment.player.username) + ' date: '+ str(self.date)