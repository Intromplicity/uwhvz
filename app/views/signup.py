from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.decorators import method_decorator

from app.models import SignupInvite, User, Player, PlayerRole
from app.util import require_post_parameters, MobileSupportedView, active_game


def signup(request, signup_invite):
    token = SignupInvite.objects.get(pk=signup_invite)
    if User.objects.filter(email=token.email).exists():
        return redirect('game_signup')
    else:
        return redirect('user_signup', signup_invite=signup_invite)


class UserSignupView(MobileSupportedView):
    desktop_template = 'registration/user_signup.html'
    mobile_template = 'registration/user_signup.html'

    def get(self, request, **kwargs):
        signup_invite = kwargs['signup_invite']
        token = SignupInvite.objects.get(pk=signup_invite)
        if token.used_at:
            messages.info(request, f'You\'ve already created an account using {token.email}.')
            return redirect('dashboard')

        return self.mobile_or_desktop(request, {'signup_invite': signup_invite})

    def post(self, request, signup_invite):
        token = SignupInvite.objects.get(pk=signup_invite)
        if token.used_at:
            messages.info(request, f'You\'ve already created an account using {token.email}.')
            return redirect('dashboard')

        first_name, last_name, password = require_post_parameters(request, 'first_name', 'last_name', 'password')
        with transaction.atomic():
            User.objects.create_user(token.email, password, first_name=first_name, last_name=last_name)
            token.used_at = timezone.now()
            token.save()

        user = authenticate(username=token.email, password=password)
        login(request, user)
        return redirect('game_signup')


@method_decorator(login_required, name='dispatch')
class GameSignupView(MobileSupportedView):
    desktop_template = 'registration/game_signup.html'
    mobile_template = 'registration/game_signup.html'

    def get(self, request):
        game = active_game()
        return self.mobile_or_desktop(request, {'game': game})

    def post(self, request):
        in_oz_pool = request.POST.get('is_oz', 'off') == 'on'
        game = active_game()
        Player.objects.create_player(request.user, game, PlayerRole.HUMAN, in_oz_pool=in_oz_pool)
        return redirect('dashboard')