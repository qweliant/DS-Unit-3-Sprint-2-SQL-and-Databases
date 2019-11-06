import sqlite3
import pandas


df = pandas.read_csv('buddymove_holidayiq.csv')
with sqlite3.connect('buddymove_holidayiq.sqlite3') as conn:
	df.to_sql('review', conn, if_exists='replace')

	cur = conn.cursor()

	query = 'SELECT COUNT(*) FROM review'
	cur.execute(query)
	result = cur.fetchone()[0]
	print(f'review has {result} rows.')

	query = 'SELECT COUNT(DISTINCT `User Id`) FROM review WHERE Nature >= 100 AND Shopping >= 100'
	cur.execute(query)
	result = cur.fetchone()[0]
	print(f' {result} users have reviewed at least 100 in Nature and Shopping')


	query = '''
		SELECT AVG(Sports) AS Sports,
			AVG(Religious) AS Religious,
			AVG(Nature) AS Nature,
			AVG(Theatre) AS Theatre,
			AVG(Shopping) AS Shopping,
			AVG(Picnic) AS Picnic
		FROM review
		'''
	cur.execute(query)
	results = cur.fetchone()
	result_dict = dict(zip([coltup[0] for coltup in cur.description], results))
	for column, value in result_dict.items():
		print(f'{column} had an average of {value:.2f} reviews.')

	cur.close()
