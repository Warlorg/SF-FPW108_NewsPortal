from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from news.models import Author


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'

    template_name = 'registration/signup.html'


@login_required
def upgrade_user(request):
    user = request.user
    group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        group.user_set.add(user)
        Author.objects.create(authorUser=User.objects.get(pk=user.id))
    return redirect('/news')
