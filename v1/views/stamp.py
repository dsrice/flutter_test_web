from rest_framework.views import APIView

from core.alert import alerts
from core.commonresponse import Build_Response
from v1.models.stamp_total import StampTotal
from v1.sirializers.article import ArticleSerializer
from v1.models.articles import Article


class StampView(APIView):
    """
    スタンプの取得APIView
    """

    def get(self, request):
        params = request.GET
        user = request.user
        stamptotal = StampTotal.objects.get(user=user)

        result_json = self.create_result_json(stamptotal)
        response = Build_Response.success_response(self, result_json)

        return response

    def create_result_json(self, stamptotal):
        """
        返信用のjson作成処理
        """
        base = {
            "loginid": stamptotal.user.loginid,
            "stamp_count": int(stamptotal.total)
        }

        return base
