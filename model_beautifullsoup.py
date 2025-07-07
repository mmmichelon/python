from bs4 import BeautifulSoup 

with open("output.txt", 'r') as myfile: 
data = myfile.read() 

soup = BeautifulSoup(data, 'html.parser') 

result = soup.find_all('font', attrs={'color': '#75751E'})
for x in result:
print(x.text.replace(" ", "").replace(" ", " ")) 

print(result) 

myfile.close()
