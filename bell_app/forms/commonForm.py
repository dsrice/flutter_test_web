from django import forms


class CommonForm(forms.Form):
    """
    共通フォーム
    """
    username = forms.CharField()
    title = forms.CharField()

    def set_base(self, request):
        username = request.user
