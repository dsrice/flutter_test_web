from django import forms


class CommonForm(forms.ModelForm):
    """
    共通フォーム
    """
    username = forms.CharField()

    def set_base(self, request):
        username = request.user