from rest_framework.views import APIView

from core.alert import alerts
from core.commonresponse import Build_Response
from v1.models.stamp_total import StampTotal
from v1.models.tokens import Token
from v1.sirializers.article import ArticleSerializer
from v1.models.articles import Article
from v1.sirializers.token import TokenSerializer


class TokenView(APIView):
    """
    スタンプの取得APIView
    """

    def post(self, request):
        params = TokenSerializer(data=request.data)
        if not params.is_valid():
            return Build_Response.error_response(self, alerts["request"]["parameter_error"], params.errors)
        print(params)
        token = Token(
            token=params.data["token"],
            user=request.user
        )
        token.save(request)

        return Build_Response.success_response(self, {})
