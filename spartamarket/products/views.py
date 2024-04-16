from django.shortcuts import render

def index(request):
	context = {"name" : "홈"}
	return render(request,'index.html',context)

def detail(request):
	context = {"name" : "상세페이지"}
	return render(request,'detail.html', context)