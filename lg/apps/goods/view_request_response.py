from .models import Goods
from .serializers import GoodsSerializer
from rest_framework.views import APIView

from rest_framework.response import Response


class GoodsListViewRequestResponse(APIView):
    def get(self, request, format=None):
        print("request.data==", request.data)
        print("request.user==", request.user)
        print("request.auth==", request.auth)
        print("request.method==", request.method)
        print("request.content_type==", request.content_type)
        print("request.query_params==", request.query_params)
        print("request.parsers==", request.parsers)

        goods = Goods.objects.all()[:10]

        goods_serializer = GoodsSerializer(goods, many=True)
        response = Response(data=goods_serializer.data)

        print("response.data==", response.data)
        print("response.status_code==", response.status_code)
        print("response.template_name==", response.template_name)

        return response
