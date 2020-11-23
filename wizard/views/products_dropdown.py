from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView

from wizard.models import Category


class ProductList(APIView):
    """
    Class to get products listing for drop down
    """
    def get(self, request):
        """
        @param request: request (HTTP obj)
        return: json response
        """
        data = list()
        categories = Category.objects.all()
        for category in categories:
            main_product = {
                'id': category.id,
                'name': category.name,
                'sub_categories': list()
            }
            sub_categories = category.subcategory_set.all()
            for sub_category in sub_categories:
                sub_category_res = {
                    'id': sub_category.id,
                    'name': sub_category.name,
                    'products': list()
                }
                main_product['sub_categories'].append(sub_category_res)
                products = list(sub_category.product_set.all().values('id', 'name'))
                sub_category_res['products'].extend(products)
            data.append(main_product)

        response = {'data': data, 'status': True, 'code': status.HTTP_200_OK}
        return JsonResponse(response)
