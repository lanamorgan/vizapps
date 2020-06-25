import json, itertools
import pandas as pd

def gen(compas, fname):
	out = open(fname, 'w')
	data = pd.read_csv(compas)
	schema ='age,c_charge_degree,race,sex,priors_count,days_b_screening_arrest,jail_length_days,out,class,cluster'.split(',')
	panel_query = "SELECT {c}, COUNT({c}) AS cnt FROM fairvis.dbo.compas GROUP BY {c};\n"
	for col in schema[:-3]:
		out.write(panel_query.format(c=col))
	# accuracy
	acc = "SELECT COUNT(CASE WHEN out=class THEN 1 END)/CAST(COUNT(*) AS float) FROM fairvis.dbo.compas GROUP BY {};\n"
	all_groups = set()
	for l in range(1,4):
		all_groups |= set(itertools.combinations(schema[:-3], l))
	for group in all_groups:
		group_list = ", ".join(group)
		out.write(acc.format(group_list))
	out.close()


def main():
	output = "out/fairvis.sql"
	compas= "../data/compas.csv"
	gen(compas, output)

if __name__ == '__main__':
	main()


# schema
# age,c_charge_degree,race,sex,priors_count,days_b_screening_arrest,jail_length_days,out,class,cluster
