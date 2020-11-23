from datetime import datetime

from django.db import transaction
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView

from wizard.models import (
    Booking,
    ProductInfo,
    Product,
    SubCategory,
    Category
)


class CreateBooking(APIView):
    """
    Class to create booking for orders
    """
    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        """
        @param request: request obj to get data (HTTP obj)
        return: return json type object (json)
        """
        try:
            data = request.data
            booking_obj = Booking()
            product_info_obj = ProductInfo()
            booking_obj.inspection = data['inspection']
            booking_obj.ref_no = data['ref_no']
            booking_obj.mobile = data['mobile']
            booking_obj.landline = data['landline']
            booking_obj.email = data['email']
            booking_obj.inspection_date = self.convert_date(data['inspection_date'])
            booking_obj.shipment_date = self.convert_date(data['shipment_date'])
            product_info_obj.name = data['product_name']
            product_info_obj.product = self.retrieve_model(data['product_id'], Product)
            product_info_obj.sub_category = self.retrieve_model(
                data['sub_category_id'], SubCategory
            )
            product_info_obj.category = self.retrieve_model(
                data['category_id'], Category
            )
            product_info_obj.units = data['unit']
            product_info_obj.purchase_order_no = data['purchase_order_no']
            product_info_obj.quantity = data['quantity']
            product_info_obj.ref_or_sku = data['ref_or_sku']
            product_info_obj.save()
            booking_obj.product_info = product_info_obj
            booking_obj.save()
            response = self.success_res()
        except Exception as exe:
            response = self.error_res()
            response['error'] = [exe.args]

        return JsonResponse(response)

    @staticmethod
    def success_res():
        """
        function to create success response
        return: response (dict)
        """
        response = dict()
        response['status'] = True
        response['code'] = status.HTTP_201_CREATED
        response['message'] = 'Created!'
        response['error'] = []
        return response

    @staticmethod
    def error_res():
        """
        function to create error response
        return: response (dict)
        """
        response = dict()
        response['status'] = False
        response['message'] = 'Error occurred while creating booking'
        response['code'] = status.HTTP_400_BAD_REQUEST
        return response

    @staticmethod
    def convert_date(date_str):
        """
        function to convert string date to date object
        @param date_str: string date (str)
        """
        if date_str:
            date = datetime.strptime(date_str, '%d-%m-%Y').date()
            return date
        return date_str

    @staticmethod
    def retrieve_model(_id, model):
        """
        function to
        """
        return model.objects.get(id=_id)
