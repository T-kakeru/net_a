import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'net_a_db.settings')

from django import setup
setup()

from net_a_db.models import Icon
p = Icon(
    icon_file_name = "icon_img/icon1_GMqarSb.PNG",
    icon_name = 'イワシ',
    icon_text = '',
)
"""
FishInfo, UserInfo
user = UserInfo.objects.get(id=1)
p = FishInfo(
    user=user,
    name="サメ",
    movie=None,
    info="半年前から海で釣りあげたサメを飼っています。40センチほど成長し元気に泳いでいます",
    gender="",
    fish_mixed="スズメダイ、貝、",
    temp=20,
    fish_size=70,
    aquarium_size=200,
    material="GEX、ことぶき水槽",
    food="アジ、さんま",
)
"""
p.save()