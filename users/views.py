from django.contrib.auth import logout
from django.shortcuts import render, redirect


def logout_view(request):
    logout(request)
    return redirect('main:index')


def register_view(request):
    if request.method != 'POST':
        form = UserRegisterForm()
    else:
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


from django.shortcuts import render

# Create your views here.
