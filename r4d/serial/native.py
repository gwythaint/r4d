import logging

from r4d.db import SerialControl

log = logging.getLogger (__name__)

def register (parent):
    log.debug ("register " + __name__)
    parent._add_model ('local', native)

class native (SerialControl):
    __mapper_args__ = {'polymorphic_identity': 'local'}

    def num_ports (self):
        return 0

    def get_udpport (self, port):
        return (port)

    def get_ttydev (self, port):
        return (port)
