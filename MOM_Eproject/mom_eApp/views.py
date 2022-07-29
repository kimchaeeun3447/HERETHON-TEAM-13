from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta
#모델 호출 : 태영
from .models import Class, User, Apply

# 메인 화면
from unicodedata import category
# 메인 화면 : 채은
def home(request):
    # /?category=마케팅
    category = request.GET.get('category', None) #쿼리스트링 없어도 됨
    print(category)

    # 상단 클래스 목록 -  로그인o -참여 예정 클래스 / 로그인x - 추천 클래스
    if request.user.is_authenticated:
        # 로그인o -참여 예정 클래스
        user_apply_list = Apply.objects.filter(user=request.user)[:2] # 2개만 조회
        user_class_list = []
        
        for apply in user_apply_list:
            item = get_object_or_404(Class, pk=apply.applyClass.id)
            user_class_list.append(item)
    else:
        #로그인x - 추천 클래스
        user_class_list = Class.objects.all()[:2] # 마감 임박 2개만 조회

    # 하단 클래스 목록 - 카테고리 필터링 포함
    if category is None:
        home_class_list = Class.objects.all()
    else:
        home_class_list = Class.objects.filter(category=category)
    
    return render(request, 'home.html', {'user_class_list': user_class_list, 'home_class_list': home_class_list, 'category': category})

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
    
    return render(request, 'mypage.html', {'user':user, 'lesson_list1':lesson_list1, 'lesson_list2':lesson_list2})
