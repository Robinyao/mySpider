# -*- coding: utf-8 -*-
import json, codecs

class LjwShDtfPipeline(object):

    def __init__(self):
        self.file = codecs.open('houses.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ',' + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
