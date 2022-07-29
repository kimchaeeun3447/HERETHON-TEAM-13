from django.shortcuts import render

# 메인 화면
def home(request):
    return render(request, 'index.html')