from django import forms
from django.forms.extras.widgets import SelectDateWidget


class IndexForm(forms.Form):
    firstName = forms.CharField(max_length=30, label='first name',required=False,help_text='f name')
    lastName = forms.CharField(max_length=30, label='last name',required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    message = forms.CharField(widget=forms.Textarea,required=False,help_text='信息')
    cc_field = forms.BooleanField(required=False,help_text='是否抄送')

    age = forms.IntegerField(max_value=110,min_value=0)

    radioselect = forms.ChoiceField(widget=forms.RadioSelect,choices=((1,'本科'),(2,'硕士'),(3,'博士')),label='学历')

    select = forms.ChoiceField(choices=((1,'本科'),(2,'硕士'),(3,'博士')),label='学历')

    multichecked = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=(('blue','blue'),('red','red')),label='多选check')
    multiselect = forms.MultipleChoiceField(choices=(('blue','blue'),('red','red')),label='多选select')

    birth_year = forms.DateField(widget=SelectDateWidget(years=('1980','1990','2000')),label='SelectData Widget')

    ddate = forms.DateField(input_formats='%Y-%m-%d')
    ddatetime = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S')

    splitDateTimeField = forms.SplitDateTimeField()

    decimalfield = forms.DecimalField(max_digits=6,min_value=0)
    floatfield = forms.FloatField(max_value=9999,min_value=-100)

    filefield = forms.FileField(allow_empty_file=True)

    filepathfield = forms.FilePathField('D:\\',recursive=False)


    imageField = forms.ImageField()


