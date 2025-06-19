import os
import logging

# set up logging
LOGPRINT = os.environ.get('LOGPRINT', 'INFO').upper()
carlog = logging.getLogger('carlog')
carlog.setLevel(LOGPRINT)
carlog.propagate = False

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(message)s'))
carlog.addHandler(handler)

# customize our logging
rpi5log = logging.getLogger('rpi5log')
# rpi5log.setLevel(?)
rpi5log.propagate = False

rpi5handler = logging.handlers.SocketHandler('172.20.10.14', 9999)
rpi5handler.setFormatter(logging.Formatter('%(message)s'))
rpi5log.addHandler(rpi5handler)