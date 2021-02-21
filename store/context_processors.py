from .models import Category, Product


def add_variable_to_context(request):
    return {
        'categories': Category.objects.all()
    }
