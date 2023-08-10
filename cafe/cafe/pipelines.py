# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CafePipeline:
    def process_item(self, item, spider):
        return item

from pyes import ES
from scrapy.utils.project import get_project_settings

ITEM_PIPELINES = ['crawler.pipelines.ElasticSearchPipeline']

class ElasticSearchPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()
        uri = "{}:{}".format(self.settings['ELASTICSEARCH_SERVER'],
                                self.settings['ELASTICSEARCH_PORT'])
        self.es = ES([uri])
    
    def process_item(self, item, spider):
        index_name = self.settings['ELASTICSEARCH_SERVER']
        self.es.index(dict(item), index_name,
                        self.settings['ELASTICSEARCH_SERVER'],
                        op_type='create')
        return item