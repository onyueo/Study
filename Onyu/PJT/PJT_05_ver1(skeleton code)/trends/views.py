from django.shortcuts import render, redirect

# Create your views here.
def keyword(request):

    return render(request, 'trends/keyword.html')


def keyword_detail(request):

    return redirect('trends:keyword')