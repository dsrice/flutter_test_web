from rest_framework.views import APIView

from core.alert import alerts
from core.commonresponse import Build_Response
from v1.sirializers.article import ArticleSerializer
from v1.models.articles import Article


class StampView(APIView):
    """
    スタンプの取得APIView
    """

    def get(self, request):
        params = request.GET
        user = request.user
        print(user)

        response = Build_Response.success_response(self, {})

        return response

    def create_result_json(self, article, next_article, prov_article):
        """
        返信用のjson作成処理
        """
        base = {
            "title": article.title,
            "body": self.convert_body(article.body),
            "article_id": article.id,
            "next_id": next_article[0].id if next_article else None,
            "prov_id": prov_article[0].id if prov_article else None,
        }

        return base
