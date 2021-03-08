import environ

import firebase_admin
from firebase_admin import credentials, messaging

from v1.models.tokens import Token

env = environ.Env()


class Firebase():
    """
    Firebase関連処理
    """
    request = None

    def __init__(self, request=None, params=None):
        self.request = request
        if (not len(firebase_admin._apps)):
            cred = credentials.Certificate(env("FIREBASE_KEY"))
            app = firebase_admin.initialize_app(cred)

    def send_multicast(self, title, body):
        """
        一括のpush通知対応
        :param title:
        :param body:
        :param ids:
        :return:
        """

        notification = messaging.Notification(
            title=title,
            body=body
        )

        android_notification = messaging.AndroidNotification(
            title=title,
            body=body
        )

        android = messaging.AndroidConfig(
            notification=android_notification
        )
        data = {
            "title": title,
            "body": body,
            "click_action": "FLUTTER_NOTIFICATION_CLICK",
            "sound": "default"
        }

        tokens = Token.objects.all().filter(is_deleted=False)

        if not tokens:
            return False

        target_tokens = list(self.__split_list(tokens, 500))

        success = 0
        failuer = 0

        for targets in target_tokens:
            base_tokens = []
            for token in targets:
                base_tokens.append(token.token)

            print(base_tokens)
            multicast_message = messaging.MulticastMessage(
                notification=notification,
                tokens=base_tokens,
                android=android,
                data=data
            )

            result = messaging.send_multicast(multicast_message)
            print(result.success_count)

        return True

    def __split_list(self, l, n):
        for idx in range(0, len(l), n):
            yield l[idx:idx + n]