from typing import Any
from django import forms
from django.contrib.auth.models import User
#from net_a_db.models import Profile, Icon

class UserForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

"""class ProfileForm(forms.ModelForm):
    website = forms.URLField(label='ホームページ')
    picture = forms.FileField(label='写真')
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['icon'].queryset = Icon.objects.all()
        # アイコンの選択肢を全てのアイコンに設定,アップデートで、同じユーザーが取得しているアイコンのみを表示させる場合Icon.objects.filter(usericon__user=user)
    class Meta():
        model = Profile
        fields = ('website', 'picture', 'icon')
"""

class LoginForm(forms.Form):
    username = forms.CharField(label='名前', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

from django import forms
from django.conf import settings
from .models import FishInfo

class FishInfoForm(forms.ModelForm):
    GENDER_CHOICES = [
        (1, '選択してください'),
        (2, 'オス'),
        (3, 'メス'),
    ]

    CATEGORY_CHOICES = [
        (1, '選択してください'),
        (2, 'アロワナ'),
        (3, 'ポリプテルス'),
        (4, 'プレコ'),
        (5, 'パクー（メチニスなど）'),
        (6, 'カラシン(テトラなど)'),
        (7, 'プラティ・卵生メダカなど'),
        (8, 'ローチ'),
        (9, 'エンゼルフィッシュ'),
        (10, 'ディスカス'),
        (11, 'シクリッド'),
        (12, 'コリドラス'),
        (13, '淡水エイ'),
        (14, 'ベタ'),
        (15, 'ナマズ'),
        (16, 'フグ'),
        (17, '川のエビ、貝、カニ'),
        (18, '汽水魚'),
        (19, 'その他熱帯魚'),
        (20, 'メダカ'),
        (21, '金魚'),
        (22, '鯉'),
        (23, '川魚'),
        (24, 'その他淡水魚'),
        (25, 'スズメダイ'),
        (26, 'ヤッコ'),
        (27, 'チョウチョウウオ'),
        (28, 'ハギ'),
        (29, 'ギンポ'),
        (30, 'ベラ'),
        (31, 'ハゼ'),
        (32, 'ハタ'),
        (33, 'フグ'),
        (34, 'エイ、サメ'),
        (35, 'タコ、イカ'),
        (36, 'クラゲ、ナマコ、ヒトデなど'),
        (37, '海のエビ、貝、カニ'),
        (38, '一般に食用魚等の魚種'),
        (39, 'その他海水魚'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="性別", required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="カテゴリー", required=False)

    class Meta:
        model = FishInfo
        fields = ['name', 'preview', 'movie', 'info', 'gender', 'category', 
                    'fish_mixed', 'temp', 'fish_size', 'aquarium_size', 'material', 'food']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '魚の名前'}),
            'info': forms.Textarea(attrs={'placeholder': '飼育情報'}),
            'category': forms.TextInput(attrs={'placeholder': 'カテゴリ'}),
            'fish_mixed': forms.TextInput(attrs={'placeholder': '混泳可能な魚'}),
            'temp': forms.NumberInput(attrs={'placeholder': '適正温度'}),
            'fish_size': forms.NumberInput(attrs={'placeholder': '魚のサイズ'}),
            'aquarium_size': forms.NumberInput(attrs={'placeholder': '飼育水槽サイズ'}),
            'material': forms.TextInput(attrs={'placeholder': 'レイアウトの情報や、使用器具'}),
            #レイアウトは別テーブル用意？
            'food': forms.TextInput(attrs={'placeholder': '餌'}),
        }