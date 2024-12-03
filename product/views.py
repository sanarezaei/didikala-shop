# from django.shortcuts import render

# from .models import Product

# def search_list(request):
#     query = request.GET.get('q')
#     products = Product.objects.search(query)
    
#     color_list = []
#     brand_list = []
#     sizes_list = []
#     child_list = []
    
#     for product in products: 
#         child_list.append(product.category)
#         brand_list.append(product.brand)
        