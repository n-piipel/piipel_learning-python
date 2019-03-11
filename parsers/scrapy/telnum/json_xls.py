from tablib import Dataset

source_path = './telnum/results/tel_spider.json'
target_path = './telnum/results/tel_spider.xls'

imported_data = Dataset().load(open(source_path).read())

with open(target_path, 'wb') as f:
    f.write(imported_data.export('xls'))
