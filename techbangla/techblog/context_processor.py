from techblog.models import Category, SubCategory


def blog_menu(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()

    return {
        'category': category,
        'subcategory': subcategory,
    }
