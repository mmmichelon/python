import requests, re, pymysql, datetime, sys, time

if __name__ == '__main__':
	condicao = True
	while(condicao):
		try:
			res = requests.get("http://meuip.com/")
			myIp = re.compile('(\d{1,3}\.){3}\d{1,3}').search(res.text).group()

			db = pymysql.connect(host="host", # your host, usually localhost
								 user="user",       # your username
								 passwd="pwd",       # your password
								 db="database")         # name of the data base

			cursor = db.cursor()

			f = open("log.txt", "a")
			f.write("INSERT INTO global_public_ip_access (ip, date, source) VALUES ( '" + myIp + "', now(), 'source' )")

			cursor.execute("INSERT INTO global_public_ip_access (ip, date, origem) VALUES ( '" + myIp + "', now(), 'source' )")
			db.commit()
			db.close()

			# if it's a insert or update, be sure to have db.commit() after the cursor.execute()
			f = open("log.txt", "a")
			f.write("done")

		except:
			condicao = False
			print(sys.exc_info()[1])
			print("stopping execution at " + str(datetime.datetime.now()))
		time.sleep(3600)