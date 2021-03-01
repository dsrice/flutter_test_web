import json
import logging
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from log_request_id import local
import datetime


class Build_Response:
    """
	レスポンス時の共通クラス
	"""

    @staticmethod
    def error_response(self, message, errors=None) -> Response:
        """
        エラー時のレスポンス作成処理
        """
        logger = logging.getLogger("error")
        if errors:
            logger.error(errors)

        result = {"errors": [message]}
        if local.__dict__.get("request_id"):
            result["process_code"] = local.request_id
        else:
            result["process_code"] = "test"

        result["server_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.error(result)

        return Response(result, message["status"])

    @staticmethod
    def success_response(self, data) -> Response:
        """
		正常時のレスポンス作成処理
		"""

        logger = logging.getLogger("main")
        result = data
        if local.__dict__.get("request_id") != None:
            result["request_id"] = local.request_id
        else:
            result["request_id"] = "test"

        result["server_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        logger.info(result)
        return Response(result)


class Exception_Manage:
    """
	例外発生時の関連共通クラス
	"""

    def log_message(self, exception) -> str:
        result = exception.__class__.__name__
        result += ": "
        result += str(exception)

        return result
