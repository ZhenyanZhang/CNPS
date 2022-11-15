import os
import sys
import re
from Bio import SeqIO



def remove_dup(list1):
    remove_list=[]
    for j,l1 in enumerate(list1):
        if j in remove_list:
            continue
        s=l1[1]
        e=l1[2]
        ident=l1[4]
        a = [str(b) for b in l1]
        remove_list1 = is_overlap(s,e,j,ident,list1,''.join(a))
        remove_list.extend(remove_list1)
    list2=[]
    for index in range(len(list1)):
        if index not in remove_list:
            list2.append(list1[index])
    return list2

def is_overlap(s,e,j,ident,list1,str0):
    remove_list = []
    for i,l1 in enumerate(list1):
        a = [str(b) for b in l1]
        str1 = ''.join(a)
        if str1==str0:
            continue
        s1=l1[1]
        e1=l1[2]
        ident1=l1[4]
        if s<e1 and e>s1:
            if ident1<=ident:
                remove_list.append(i)
            else:
                remove_list.append(j)
                ident=ident1
                j=i
    return remove_list


bin_file = sys.argv[1]
outdir = sys.argv[2]
dbfile = 'CNPSK.prot.fa'
dbfile_ann = 'CNPSK.fa.id'
ann_dict = {}
f=open(dbfile_ann)
lines = f.readlines()
for line in lines:
    data = line.strip().split('~')
    ann_dict[data[0]] = data
f.close()

if not os.path.exists(outdir):
    os.mkdir(outdir)
  

cmd = "diamond blastx --quiet -p {} -q {} -d {} -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore slen --id 70 -o {}/diamond.out".format(8,bin_file,dbfile,outdir)
#print(cmd)
os.system(cmd)
diamond_result = os.path.join(outdir,"diamond.out")
mge_result = os.path.join(outdir,"mge.xls")


dd1={}
tmp={}
f=open(diamond_result)
lines = f.readlines()
for line in lines:
    data = line.strip().split('\t')
    q_id = data[0]
    s_id = data[1]
    identity = float(data[2])
    aln_length = int(data[3])
    start = data[6]
    end = data[7]
    sstart = int(data[8])
    send = int(data[9])
    cov = round(abs(int(data[8])-int(data[9]))*100/float(data[-1]),3)
    if cov<60:
        continue
    if sstart>send:
        sstart,send=send,sstart
        strand='-'
    else:
        strand='+'
    if q_id not in tmp:
        tmp[q_id] = []
    tmp[q_id].append([s_id,sstart,send,strand,identity])
    if q_id not in dd1:
        dd1[q_id]={}
    dd1[q_id][s_id]=line.strip()+'\t'+str(cov)
f.close()

w = open(mge_result,'w+')
w.write('qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore slen'.replace(' ','\t')+'\tcov\tgene\ttype\n')
for k,vs in tmp.items():
    keep_v = remove_dup(vs)
    for v in keep_v:
        s_id = v[0]
        infos = ann_dict[s_id]
        w.write(dd1[k][s_id]+'\t'+infos[1]+'\t'+infos[2]+'\n')
w.close()