import sys
import os
from StringIO import StringIO
from lxml import etree

if not len(sys.argv) > 2:
    raise Exception(
        'You must supply 2 arguments:\n\t1) the XML file to be transformed\n\t2)'
        ' the XSL styling file')
elif '.xml' not in sys.argv[1]:
    raise Exception('The first argument must be an XML file')
elif '.xsl' not in sys.argv[2]:
    raise Exception('The second argument must be an XSL file')

xml_file = sys.argv[1]
xsl_file = sys.argv[2]

with open(xml_file) as m, open(xsl_file) as s:
    xml, xsl = m.read(), s.read()

mtree, stree = etree.XML(xml), etree.XML(xsl)

transform = etree.XSLT(stree)
result = transform(mtree)
html_file = '{}.html'.format(xml_file).replace('.xml', '')
result.write(html_file)
os.system('open {}'.format(html_file))
