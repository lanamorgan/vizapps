import json, itertools
import pandas as pd

def gen(compas, fname):
	out = open(fname, 'w')
	data = pd.read_csv(compas)

	# generate queries
	out.close()


def main():
	output = "out/fairvis.sql"
	compas= "../data/compas.csv"
	gen(compas output)

if __name__ == '__main__':
	main()
