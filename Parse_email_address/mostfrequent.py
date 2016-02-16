#!/usr/bin/python
fname= raw_input('\nEnter the path for the text file containing emails: \n')
handle = open(fname)
count = 0
list1=[]
list2=[]
for line in handle:
    list1=line.split()
    if not list1: continue
    elif list1[0]=='From':
        list2.append(list1[1])
    del list1[:]

my_dict = {i:list2.count(i) for i in list2}
list1= sorted(my_dict.values())

print '\nFollowing are the email addresses and their respective frequency:\n'
for (x, y) in my_dict.iteritems():
    print '\nEmail address: {}, Frequency: {}\n'.format(x,y)
print ('\n----------------------------------------------------------------------------\n')


for (k, v) in my_dict.iteritems():
    if v == list1[(len(list1)-1)]:
        print '\nThe most frequent emaill is from: {} and appears {} times in the file\n'.format(k,v)



