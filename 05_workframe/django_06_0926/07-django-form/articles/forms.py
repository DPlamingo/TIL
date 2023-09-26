from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)  # 제목, max는 필수인자가 아님
#     content = forms.CharField(widget=forms.Textarea) # 내용
    

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title'
            }
        )
    )
    
    # model 등록
    class Meta:  # 문법
        model = Article # 등록하면 알아서 해석함
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)