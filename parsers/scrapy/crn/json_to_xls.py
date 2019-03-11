import pandas

source_path = './crn/results/base_crn.json'
target_path = './crn/results/base_crn.xls'

pandas.read_json(source_path).to_excel(target_path)
