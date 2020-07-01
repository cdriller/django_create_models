import json
from models.models import Company


if __name__ == '__main__':
	with open('sample_data/sample_companies.json') as f:
		sample_data_as_json = json.load(f)

	for element in sample_data_as_json:
		company = Company(name=element['name'], strasse=element['strasse'], plz=element['plz'], ort=element['ort'], land=element['land'])
		company.save()