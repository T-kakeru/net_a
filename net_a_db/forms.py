from typing import Any
from django import forms
from django.contrib.auth.models import User
from net_a_db.models import Profile, Icon

class UserForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    website = forms.URLField(label='ホームページ')
    picture = forms.FileField(label='写真')
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['icon'].queryset = Icon.objects.all()
        # アイコンの選択肢を全てのアイコンに設定,アップデートで、同じユーザーが取得しているアイコンのみを表示させる場合Icon.objects.filter(usericon__user=user)
    
    class Meta():
        model = Profile
        fields = ('website', 'picture', 'icon')

class LoginForm(forms.Form):
    username = forms.CharField(label='名前:', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード確認', widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが一致していません')