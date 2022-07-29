from django.shortcuts import render, get_object_or_404

#모델 호출 : 태영
from .models import Class
from .models import User
from .models import Apply

# 메인 화면
def home(request):
    return render(request, 'index.html')

# 클래스 디테일 화면 : 태영
def detail(request, lesson_id):
    lesson = get_object_or_404(Class, pk=lesson_id)
    apply = get_object_or_404(Apply)
    return render(request, 'detail.html', {'lesson':lesson, 'apply':apply})


# 클래스 등록 화면 : 태영
def apply(request, lesson_id):
    lesson = get_object_or_404(Class, pk=lesson_id)
    return render(request, 'apply.html', {'lesson':lesson})