from rest_framework.views import APIView

from core.commonresponse import Build_Response
from v1.sirializers.article import ArticleSerializer
from v1.models.articles import Article


class ArticleView(APIView):
    """
    記事一覧の取得APIView
    """

    def get(self, request):
        params = request.GET
        print(params)
        articles = Article.objects.all().order_by("-id")

        response_data = {
            "articles": self.create_result_json(articles)
        }
        response = Build_Response.success_response(self, response_data)
        return response

    def create_result_json(self, articles):
        """
        返信用のjson作成処理
        """
        result = []
        for article in articles:
            base = {
                "title": article.title,
                "body": article.body,
                "article_id": article.id
            }
            result.append(base)

        return result
