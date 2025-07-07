import pymysql
import datetime, io, json, codecs, sys
import chardet

encoding = "utf-8"

def log(var): print(str(datetime.datetime.now()) + " " + str(var))

db = pymysql.connect(host="localhost", user="tr1pl3m", passwd="root", db="mmsyst")#, charset='utf8', use_unicode=True)

cur_temp = db.cursor()
cur_empresa = db.cursor()

control = 0

cur_temp.execute("select str_telefone from tb_telefone")
count = 0

farray = []

i = 0
j = 0
f_json = ""

telefone_concatenacao = ""

for row in cur_temp.fetchall():
	code  = row[0]
	empresa = row[0]

	cur_empresa.execute("SELECT id_telefone, id_main FROM tb_telefone WHERE str_telefone = '" + empresa + "'")

	if cur_empresa.rowcount > 1:
		for rowx in cur_empresa.fetchall():
			telefone_concatenacao = telefone_concatenacao + ", " + str(rowx[0])
		log(cur_empresa.rowcount)
		count = count + 1


file = open('telefone', 'w')
file.write(telefone_concatenacao)
file.close()

log(count)
#db.commit()
db.close()