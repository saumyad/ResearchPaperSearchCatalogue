__author__ = 'amitpanda'
# coding: utf-8

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    randomstr = retstr.getvalue()
    retstr.close()
    return randomstr

def num_of_spaces(row):
    count=0
    for char in row:
        if char==' ':
            count+=1
    return count

def comma_count(row):
    count=0
    for char in row:
        if char==',':
            count+=1
    return count

def clean_text(text):   
    randomstr = text.replace('\n', ' ').replace('\r', ' ')
    randomstr = re.sub('[^a-zA-Z0-9-_*:. ]', '', randomstr)
    return randomstr

def parse(string_mine):
    #inf = open(file)
    abstract_done = False
    abstract_print = False
    references_done = False
    references_print = False
    inf = string_mine
    inf_list = inf.split('\n')
    abstract_str = ''
    references_str = ''
    for row in inf_list:
        #print row
        if abstract_print ==True:
            row_list = row.split(" ")
            if "Categor" in row_list[0] or "INTRODUCTION" in row_list[0] or "CATEGOR" in row_list[0] or "Introduction" in row_list[0] or "Keywords" in row_list[0]:
                abstract_print = False
                continue
            else:
                row = row.replace('\n', ' ')
                #print row
                abstract_str = abstract_str + row + ' '

        if "ABSTRACT" in row or "Abstract" in row and abstract_done==False:
            print "---------------ABSTRACT-------------"
            new_row = row.replace("Abstract","",1).replace('\n',' ')
            print new_row
            abstract_done = True
            abstract_print = True

        if "REFERENCES" in row and references_done==False:
            print "--------------REFERENCES-------------"
            references_print = True
            references_done = True

        if references_print == True:
            if "[9]" in row:
                references_print = False
            else:

                row = row.replace('\n',' ')
                #print row
                #references_list.append()
                references_str = references_str + row + ' '

    ref_list = []

    print type(references_str)
    #references_str = references_str.replace('\n',' ')
    print references_str
    initial_ref_list = references_str.split(' ')
    print "INITTTTTTTTTTT", initial_ref_list
    final_ref_list=[]
    x=0
    while x<len(initial_ref_list):
        if initial_ref_list[x]=='[1]':
            x += 1
            temp_list=[]
            while initial_ref_list[x]!='[2]':
                temp_list.append(initial_ref_list[x])
                x += 1
            temp_str = ' '.join(temp_list)
            final_ref_list.append(temp_str)
            x+=1
            temp_list=[]
            while initial_ref_list[x]!='[3]':
                temp_list.append(initial_ref_list[x])
                x += 1
            temp_str = ' '.join(temp_list)
            final_ref_list.append(temp_str)
            x+=1
            temp_list=[]
            while initial_ref_list[x]!='[4]':
                temp_list.append(initial_ref_list[x])
                x += 1
            temp_str = ' '.join(temp_list)
            final_ref_list.append(temp_str)
            x+=1
            temp_list=[]
            while initial_ref_list[x]=='[1]' or initial_ref_list[x]=='[2]' or initial_ref_list[x]=='[3]' or initial_ref_list[x]=='[4]' or initial_ref_list[x]=='[5]':
                temp_list.append(initial_ref_list[x])
                x += 1
            temp_str = ' '.join(temp_list)
            final_ref_list.append(temp_str)
        else:
            x+=1

    print "FINALLLL REF LISTTTT :" #len(final_ref_list), final_ref_list
    for y,x in enumerate(final_ref_list):
        ref_list.append(x)

#Stop editting!
    title = ''
    count=0
    for row in inf_list:
        if count==0:
            if row!='':
                title = title + row
        elif count==1:
            if row=='':
                title += ' '
            else:
                if num_of_spaces(row)>=2:
                    title += ' '+row
        elif count==2:
            if num_of_spaces(row)>=2 and comma_count(row)<2:
                title = title + row
            else:
                break
        count +=1

    count=0
    abstract_started=False
    author_list=[]
    final_author_list=[]
    flag2=True
    for row in inf_list:

        #print row, "Count :", comma_count(row), abstract_started
        if "ABSTRACT" in row or "Abstract" in row:
                abstract_started = True
        if count>0 and abstract_started==False:
            if len(row)>4 and len(row)<25 and num_of_spaces(row)==1 and ',' not in row and 'University' not in row:
                author_list.append(row)
                flag2=False
            elif comma_count(row)>=2 and flag2==True:
                flag2=False
                list = row.split(',')
                list = [x.strip() for x in list]
                print "LIST :::", list
                for element in list:
                    if num_of_spaces(element)==1 or num_of_spaces(element)==2 and len(element)>=5:
                        author_list.append(element)
        count += 1

    for author in author_list:
        author = author.decode('unicode_escape').encode('ascii','ignore')
        author = author.rstrip('1234567890')
        final_author_list.append(author)
        print author

    print "-----AUTHOR LIST------"
    # print author_list
    print final_author_list

    print "-----TITLE-------"
    print title
    return clean_text(title), clean_text(abstract_str), ref_list, final_author_list


# path = 'paper10.pdf'
# text = convert_pdf_to_txt(path)
# print text

# abstract_str, references_str = parse(text)
# f = open("abstract.txt","wb")
# f.write(abstract_str)
# f1 = open("references.txt","wb")
# f1.write(references_str)

