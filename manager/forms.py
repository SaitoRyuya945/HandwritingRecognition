from django import forms


# フォームの定義
# ファイルアップロードするフォーム
class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50, empty_value='output')
    file = forms.FileField(widget=forms.FileInput(attrs={'onchange': 'previewImage(this)'}))


class UserForm(forms.Form):
    areaone = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'id': 'resultbase64',
                "rows": 20,
                "cols": 10,
            }
        )
    )
