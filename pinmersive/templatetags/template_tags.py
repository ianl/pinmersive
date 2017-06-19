from django import template
from categories.models import Category

register = template.Library()

# Simple Tags
@register.simple_tag
def get_categories():
    return Category.objects.all()


# Filter Tags
@register.filter
def is_following_user_profile(value, arg):
    return value.is_following_user_profile(arg)

@register.filter
def is_following_board(value, arg):
    return value.is_following_board(arg)