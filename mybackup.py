#!/usr/bin/env python

import ConfigParser
from datetime import datetime
import logging
import logging.config
import sys


def main():
    logging.config.fileConfig('logging.conf')

    try:
        start_time = datetime.now()
        logging.info('Started')

        config = ConfigParser.RawConfigParser()
        config.read('application.conf')

        finish_time = datetime.now()
        logging.info('Finished, time consumed: %s', finish_time - start_time)

    except Exception as e:
        e_type, _, e_traceback = sys.exc_info()
        message = '{0} ({2}:{3}): {1}'.format(e_type.__name__, e, e_traceback.tb_frame.f_code.co_filename, e_traceback.tb_lineno)
        sys.stderr.write(message)
        logging.error(message)

if __name__ == '__main__':
    main()
