import json, itertools, random
import pandas as pd

def gen(votes, pols, fname):
	out = open(fname, 'w')
	dates = pd.read_csv(votes)['date'].unique()
	person_id = pd.read_csv(pols)['pid'].unique()

	q1 = "SELECT date, count(vid) as vote_count FROM icheck.dbo.votes GROUP BY 'date';\n"
	out.write(q1)
	q2 = "SELECT pols.pid, pols.party, COUNT(CASE WHEN pol_votes.vote=person_votes.vote THEN 1 END) / CAST(COUNT(*) as FLOAT) AS agree_per FROM (SELECT * FROM icheck.dbo.pol_votes, icheck.dbo.votes WHERE vote_id = vid AND person_id = '{}' AND date BETWEEN '{}' AND '{}') AS person_votes, icheck.dbo.pol_votes pol_votes, icheck.dbo.pols pols WHERE pol_votes.vote_id=person_votes.vote_id AND pol_votes.person_id=pols.pid GROUP BY pols.pid, pols.party;\n"

	small_people = random.sample(list(person_id), 8)
	# small_dates = random.sample(list(dates), 11)

	for pid in small_people:
		small_dates = random.sample(list(dates), 8)
		for pair in itertools.product(small_dates, small_dates):
			mini, maxi = pair
			out.write(q2.format(pid, mini, maxi))
	out.close()

def main():
	output = "out/icheck_tiny.sql"
	dates = "../data/votes_small.csv"
	pols = "../data/pols_small.csv"
	gen(dates, pols, output)

if __name__ == '__main__':
	main()










