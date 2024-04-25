from django import template
from cartsapp.models import Cart
from cartsapp.utils import get_user_carts


register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)
    
    