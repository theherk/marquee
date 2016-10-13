#!/usr/bin/env python
import logging

from marquee.formatter import MarqueeFormatter
from marquee.handler import CloudWatchEventsHandler

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

handler = CloudWatchEventsHandler(detail_type='new_type')
log.addHandler(handler)

fmt = MarqueeFormatter('theherk.testapp')
handler.setFormatter(fmt)

log.info('Hello. This is dog.')
