from django.forms import ModelForm, Textarea, TextInput
from ..models import Article, Author

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields=['name','age']

class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields = ['title','content','author','pub_date']
        # 修改默认组件类型
        widgets = {
            'content' : Textarea(attrs={'cols': 80, 'rows': 10}),
            'author' : TextInput(attrs={'readonly':True})
        }
        # 全面定制化
        labels = {
            'title': ('标题'),
        }
        help_texts = {
            'title': ('请输入标题.'),
        }
        error_messages = {
            'title': {
                'max_length': ("标题字段超长了."),
            },
        }
