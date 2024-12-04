# from django.shortcuts import render

# from .models import Product
# from variant.models import Variants

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
#         if product.variant == 'Color':
#             variant = Variants.objects.filter(product_id=product.id)
#             for var in variant:
#                 color = var.color
#                 color_list.append(color)
#         if product.variant == 'Size':
#             variant = Variants.objects.filter(product_id=product.id)
#             for var in variant:    
#                 size = variant.size
#                 sizes_list.append(size)
#         if product.variant == 'Size-Color':
#             variant = Variants.objects.filter(product_id=product.id)
#             for var in variant:
#                 size = var.size
#                 color = var.color
#                 sizes_list.append(size)
#                 color_list.append(color)
                
#     colors = [i for n, i in enumerate(color_list) if i not in \
#         color_list[n + 1:]] 
#     sizes = [i for n, i in enumerate(sizes_list) if i not in sizes_list[n + 1:]]
#     brands = [i for n, i in enumerate(brand_list) if i not in \
#         brand_list[n + 1:]] 
#     childs = [i for n, i in enumerate(child_list) if i not in \
#         child_list[n + 1:]]
