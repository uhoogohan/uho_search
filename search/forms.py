from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(label="", required=False, max_length=150,
        widget=forms.TextInput(attrs={'placeholder': '検索して'}))

class UploadForm(forms.Form): # アップロードフォーム
    file = forms.FileField(required=True, label='')