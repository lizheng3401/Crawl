import sys

from scrapy import cmdline

print(sys.argv)
sys.argv.pop(0)
cmdline.execute(sys.argv)