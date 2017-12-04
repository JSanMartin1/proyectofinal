from django.shortcuts import redirect

def redirecthome(request):
    return redirect('/store')
