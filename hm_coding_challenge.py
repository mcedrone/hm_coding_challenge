import argparse
import csv
from decimal import Decimal

def parse_file(file_name):
	with open('challenge_dataset.csv','rb') as csvfile:
		country_revenue_map = {}
		revenue_by_keyword_map = {}
		
		reader = csv.reader(csvfile, delimiter=',')
		row_count = 0
		skipped_lines = 0
		country = None
		for row in reader:
			if row_count == 0: #skip header
				row_count += 1
				continue
			
			if row[1]:
				country = row[1]
				if country not in country_revenue_map:
					country_revenue_map[country] = 0
			else:
				try:
					row_revenue = Decimal(row[3].strip().replace('$',''))
				except:
					skipped_lines += 1
					print("skipping row "+str(row))
				
				country_revenue_map[country] += row_revenue

				keyword = row[2].split(' - ')
				for keyword in keyword:
					if " and " in keyword:
						keyword = keyword.replace(' and ',' ')
						keyword_array = keyword.split(' ')
					elif " " in keyword:
						keyword_array = keyword.split(' ')
					else:
						keyword_array = [keyword]

					for k in keyword_array:
						if k not in revenue_by_keyword_map:
							revenue_by_keyword_map[k] = 0
						revenue_by_keyword_map[k] += row_revenue

		print("Skipped "+str(skipped_lines)+" with poor data")

		print("Revenue by country: "+str(country_revenue_map))
		print("Revenue by keywords: "+str(revenue_by_keyword_map))

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("file_name", help="file_name to get data from")
	args = parser.parse_args()
	parse_file(args.file_name)

if __name__ == '__main__': main()
