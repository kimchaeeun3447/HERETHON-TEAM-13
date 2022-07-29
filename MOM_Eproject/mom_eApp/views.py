from django.shortcuts import render, get_object_or_404

#모델 호출 : 태영
from .models import Class

# 메인 화면
def home(request):
    return render(request, 'index.html')

# 클래스 디테일 화면 : 태영
def detail(request, lesson_id):
    lesson = get_object_or_404(Class, pk=lesson_id)
    return render(request, 'detail.html', {'lesson':lesson})