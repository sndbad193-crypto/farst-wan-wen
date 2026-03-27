import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Origin Description
origin_old = 'وتفتخر بانتمائها إلى فروع "آل درويش" و"آل صالح"'
origin_new = 'وتفتخر بانتمائها إلى فروع "آل درويش" و"آل صالح" و"آل الحياكة"'
content = content.replace(origin_old, origin_new)

# 2. Add Seed Member for Al-Hyake
seed_old = "{ id: 'HY-10201', name: 'أحمد جاسم الحياني', status: 'active', date: '٢٠٢٤/٠١/١٢', meta: { rank: 'شيخ', hijri: '١٤٤٥/٠٦/٢٨' }, gov: 'بغداد' },"
seed_new = "{ id: 'HY-10201', name: 'أحمد جاسم الحياني', status: 'active', date: '٢٠٢٤/٠١/١٢', meta: { rank: 'شيخ', hijri: '١٤٤٥/٠٦/٢٨' }, gov: 'بغداد' },\n                    { id: 'HY-55670', name: 'ياسين محمود الحياكة', status: 'active', date: '٢٠٢٤/٠٤/١٠', meta: { rank: 'فرد' }, gov: 'بغداد', subTribe: 'فرع الحياكة' },"
content = content.replace(seed_old, seed_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
