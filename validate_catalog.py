import sys
import os
import re
from pprint import pprint, pformat
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from config import Main
from logger import logger
import logging
logger.setLevel(logging.DEBUG)
from utils import html_tags, html_tag_regex

class Base(object):

    def __iter__(self):
        home_dir = Main().get('HEADWAY', 'home_dir')
        if __name__ == '__main__':
            if len(sys.argv) > 1:
                home_dir = sys.argv[1]
            else:
                raise Exception(
                    'You must supply 1 argument (the path to the files '
                    'you want to validate)')
        for curr, dirs, files in os.walk(home_dir):
            for f in files:
                if f.endswith('.xml'):
                    with open(curr + os.sep + f) as _:
                        lines = _.readlines()
                    with open(curr + os.sep + f) as _:
                        doc = _.read()
                    yield curr + os.sep + f, doc, lines

class Tags(Base):

    def __getitem__(self, item):
        results = []
        for path, doc, lines in self:
            soup = BeautifulSoup(doc, 'lxml')
            help(soup.find_all)
            items = soup.find_all(item)
            if not items:
                continue
            results.append((path, items))
        return results

class HTMLTables(Base):
    pass

class BrokenHTMLTags(HTMLTables):
    bad_pattern = re.compile(
        '<?[' + html_tag_regex + ']\w*>.*(</[' + html_tag_regex + '][A-Za-z0-9]*>)')
    bad_pattern = re.compile(
        '<?[' + html_tag_regex + ']\w*>.*(</[' + html_tag_regex + ']\w*>)')

    def __init__(self):
        for path, res in CDATA():
            for elem in res:
                text = elem[1]
                count = len([tag_name for tag_name in html_tag_regex.strip('[')[:-4].split('|') if tag_name in text])
                # print count
                # for tag_name in html_tag_regex.strip('[')[:-4].split('|'):
                #     if tag_name in text and re.search('[<|</]+' + tag_name + '>+', text):
                #         count += 1
                # for i in range(count):
                # pattern = re.compile('(<+)(' + html_tag_regex + ')(>+).*(<+/+)(' + html_tag_regex + ')(>+)')
                pattern = re.compile('\w*(<+)(' + html_tag_regex + ')(>+)')
                match = pattern.search(text)
                if match and len(match.groups()) != 3:
                    # if len(match.groups()) % 6 != 0:
                    print match.groups(), len(match.groups())

class EscapedAmpersandsInCDATA(Base):

    def __init__(self):
        for path, res in CDATA():
            

class TridionIDs(Base):

    def get(self):
        results, count = [], 0
        for path, doc, lines in self:
            tridionids = re.findall('<(\w+)\s.*(tcm:\d*-\d*)', doc)
            for i, res in enumerate(tridionids):
                tag, _id = res
                for j, line in enumerate(lines):
                    if _id in line:
                        tridionids[i] = [j + 1] + list(tridionids[i])
                        if len(tridionids[i]) > 3:
                            tridionids[i].pop(0)
            temp = tridionids[:]
            for i, _id in enumerate(temp):
                temp[i] = '|'.join([str(t) for t in temp[i]])
            temp = list(set(temp))
            tridionids = [t.split('|') for t in temp]
            for _id in tridionids:
                _id[0] = int(_id[0])
            results.append((path, sorted(tridionids)))
            count += len(results)
        return tuple(results), count

    def is_present_in_every_element(self):
        pass

class CDATA(Base):

    def __iter__(self):
        results = []
        for path, doc, lines in Base.__iter__(self):
            result = re.findall('<(.*)><!\[CDATA\[(.*)\]\]><', doc)
            if result:
                results.append((path, result))
        return (item for item in results)

if __name__ == '__main__':
    # pprint(Tags()['table'])
    # HTMLTables()
    # pprint(TridionIDs().get())
    # pprint(CDATA().get())
    BrokenHTMLTags()
