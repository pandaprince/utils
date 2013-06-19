import sys
import os
import pickle

def read_from_file(f, seperator=','):
    for line in f:
        yield line.strip().split(seperator)

class IndexTranslator:
    def __init__(self):
        self.index = {}

    def idx(self, key, allow_update=True):

        if allow_update and key not in self.index:
            self.index[key] = len(self.index) + 1
        return self.index.get(key,None)

def main(infolder):
  ip_dict = IndexTranslator()
	time_dict = IndexTranslator()
	cat_dict = IndexTranslator()
	subcat_dict = IndexTranslator()	
	for filename in os.listdir(infolder):
		print '%s\t' %(infolder+filename)
		for splits in read_from_file(file(infolder+filename)):
			assert(len(splits) == 8)
			ip_id = ip_dict.idx(splits[0]);
			time_id = time_dict.idx(splits[1]);
			cat_id = cat_dict.idx(splits[5]);
			subcat_id = subcat_dict.idx(splits[6]);
			assert(ip_id is not None);
		print '%s\t%d' %(filename, len(ip_dict.index))

