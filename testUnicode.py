#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

foo = u'สวัสดี...'
print foo.encode('utf-8')

#a = set([1,2])
#a = {1, 2, 3}
#b = {1:2, 3:4}
#print a
#print type(a)
#print b, type(b)
#print type({})

# f = open('out.txt', 'w')
# print >> f, 'Filename:', "fsjdk"  # or f.write('...\n')
# f.close()

# f = open('test3', 'w')
# f.write(foo.encode('utf-8'))
# f.close()

# f = codecs.open('test', 'w', 'UTF-8')
# f.write(foo)
# f.close()

# old_stdout = sys.stdout # save it, in case we need to restore it 
# sys.stdout = open("test2", 'w')
# print u"รักนะ".encode('utf8')

# sys.stdout = old_stdout
# print "end file"

