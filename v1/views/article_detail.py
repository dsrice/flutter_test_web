from rest_framework.views import APIView

from core.alert import alerts
from core.commonresponse import Build_Response
from v1.sirializers.article import ArticleSerializer
from v1.models.articles import Article


class ArticleDetailView(APIView):
    """
    記事詳細の取得APIView
    """

    def get(self, request):
        params = request.GET
        print(params)
        target_id = params.get(key="article_id", default=None)
        print(target_id)
        if target_id:
            article = Article.objects.get(id=target_id)
            next_article = Article.objects.filter(id__gt=target_id, is_deleted=False)[:1]
            prov_article = Article.objects.filter(id__lt=target_id, is_deleted=False).order_by('-id')[:1]
            print(next_article)

            response_data = self.create_result_json(article, next_article, prov_article)

            response = Build_Response.success_response(self, response_data)
        else:
            response = Build_Response.error_response(self, alerts["request"]["parameter_error"], )
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

    def convert_body(self, body):
        """
        画像へのリンクを修正する
        :param body:
        :return:
        """
        if "/media/django-summernote/" in body:
            return body.replace("/media/django-summernote/", "http://10.0.2.2:8000/media/django-summernote/")
        else:
            return body