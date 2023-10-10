import logging
import time
import json
import sys

from gmaps.downloader import wgs_to_tile, get_url

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


def get_urls(line):
    datain = json.loads(line)
    server = datain['server']
    start_col = datain['pos1y']+datain['start_col']
    end_col = start_col + datain['subsize']
    start_row = datain['pos1x']+datain['start_row']
    end_row = start_row + datain['subsize']
    urls = [get_url(datain['server'], i, j, datain['zoom'], datain['style']) \
        for j in range(start_col,end_col) \
            for i in range(start_row, end_row)]
    return urls



# ---------------------------------------------------------
if __name__ == '__main__':
    for line in sys.stdin:
        print(get_urls(line))
        
           


