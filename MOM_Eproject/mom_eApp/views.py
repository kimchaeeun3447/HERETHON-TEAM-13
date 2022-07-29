from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta
#모델 호출 : 태영
from .models import Class, User

# 메인 화면
def home(request):
    return render(request, 'index.html')

# 클래스 디테일 화면 : 태영
def detail(request, lesson_id):
    lesson = get_object_or_404(Class, pk=lesson_id)
    return render(request, 'detail.html', {'lesson':lesson})

#마이페이지 화면 : 하린
def mypage(request, user_id):
    
    user = get_object_or_404(User, pk=user_id)

    #참여 예정 클래스

    lesson_list1 = Class.objects.filter(class_start_time__range=[date.today(), date.today() + timedelta(days=30)]).all()


    #참여한 클래스
    lesson_list2 = Class.objects.filter(class_start_time__range=[date.today() - timedelta(days=30), date.today()]).all()[:3][::-1]
    
    return render(request, 'mypage.html', {'lesson_list1':lesson_list1, 'lesson_list2':lesson_list2})