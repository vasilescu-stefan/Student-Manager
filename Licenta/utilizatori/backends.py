from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel=get_user_model()

class NrMatricolBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get( Q(username__iexact=username) | Q(nr_matricol__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(nr_matricol__iexact=username)).order_by("id").first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
            
