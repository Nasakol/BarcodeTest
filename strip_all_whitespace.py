def deleteall(lst_string):
	cnt = 1
	while lst_string.count('') > 0 :
		lst_string.remove('')
		cnt += 1

def strip_all_whitespace(s):
	delimeter_list = ['\t', 'a', " "]

	for deli in delimeter_list :
		lst = s.split(deli)
		deleteall(lst)
		s = ' '.join(lst)

	for x in lst :
		print x

if __name__ == "__main__" :
	s = "    bcd efgh   ijka      	mnop	zzzzaaayyyy    "
	# strip_all_whitespace(s)
	lst = list(s)
	print lst
	print s
	s = s.replace(' ', '')
	s = s.replace('\t', '')
	print s
