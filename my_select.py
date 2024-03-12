import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'net_a_db.settings')

from django import setup
setup()

from net_a_db.models import FishInfo
fishinfos = FishInfo.objects.filter(name='サメ').all()

for fishinfo in fishinfos:
    print(fishinfo.name, fishinfo.info)

"""
アイコン情報を全権取り出し
from net_a_db.models import Icon
icons = Icon.objects.all()
for icon in icons:
    print(icon.icon_file_name, icon.icon_name, icon.icon_text)
"""
"""
一件のfishinfoを表示
from net_a_db.models import FishInfo
fishinfo = FishInfo.objects.get(id=1)
print(
    fishinfo.name, fishinfo.movie,
    fishinfo.info, fishinfo.fish_size,
    fishinfo.gender, fishinfo.fish_mixed,
    fishinfo.temp, fishinfo.fish_size,
    fishinfo.aquarium_size, fishinfo.material,
    fishinfo.food)
"""
