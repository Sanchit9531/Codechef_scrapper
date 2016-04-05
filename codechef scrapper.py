import urllib 
import bs4
from BeautifulSoup import BeautifulSoup
import os
def downloadcode(url,qname,user,codeid,no):
    #path='G:\Python scrapper
    #print url
    source=urllib.urlopen(url).read()
    soup=bs4.BeautifulSoup(source,"html.parser")
    txt=soup.find('pre')
    directory='C:\Users\homes\Desktop\codechef scrapper/'+user+'/'+qname
    if not os.path.exists(directory):
        os.makedirs(directory)    
    fobj = open(directory+'/'+qname+'('+str(no)+')'+'.html', 'w')
    fobj.write(str(txt))
    fobj.close()
    codeid=codeid.replace('status','problems')
    codeid=codeid.replace(','+user,'')
    question=urllib.urlopen(codeid).read()
    fobj = open(directory+'/'+'(Question)'+qname+'.html', 'w')
    fobj.write(str(question))
    fobj.close()

    
def downloadlinks(codeid,qname,user):
    url="https://www.codechef.com"+codeid

    #print url
    
    source=urllib.urlopen(url).read()
    soup=bs4.BeautifulSoup(source,"html.parser")
   # li=[cl for l in soup.findAll('tbody') for cl in l.findAll('tr') if(cl['class'][0].encode("ascii")=='kol')]
    li=[]
    for l in soup.findAll('tbody'):
        for cl in l.findAll('tr'):
            #print cl.findAll('a')[1]['href']
            clas=cl.get('class')
            clas[0]=clas[0].encode("ascii")
            if(clas[0]=='kol'):
                clstr=str(cl)
                if clstr.find('tick-icon.gif')!=-1:
                    link=cl.findAll('a')[1]['href']
                    li.append(link)
    li=["https://www.codechef.com"+l.encode("ascii").replace("viewsolution","viewplaintext") for l in li]
    j=0;
    #print li
    for i in li:
        downloadcode(i,qname,user,url,j)
        j+=1

user =raw_input("Enter the username \n")
#user="alpha_engineer"
url="https://www.codechef.com/users/"+user

print url

source=urllib.urlopen(url).read()
soup=bs4.BeautifulSoup(source,"html.parser")
#link_list=[l.get('href') for l in soup.findAll('a') if user in l]
j=1
for l in soup.findAll('a'):
    f=l.get('href')
    if f.find(','+user,len(l))!=-1 and f.find('status',len(l))!=-1:
      #  print f
        qname=f[f.find('status',len(l))+7:f.find(','+user,len(l))]
        print str(j)+'.) '+qname+' ',
      #  print qname
        downloadlinks(f,qname,user)
        print '..........Done\n'
        j+=1
#link_list=first_tag.get('href')
#print link_list
