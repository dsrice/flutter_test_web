from rest_framework import status

alerts = {
    "request": {
        "parameter_error": {
            "status": status.HTTP_400_BAD_REQUEST,
            "code": 400,
            "message": "リクエスト内容が異常です"
        },
        "internal_error": {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "code": 500,
            "message": "内部エラー"
        }
    },
}