#!/usr/bin/env python
import json
import logging

from marquee.formatter import MarqueeFormatter, MarqueeEventFormatter
from marquee.handler import CloudWatchEventsHandler

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

handler = CloudWatchEventsHandler(detail_type='new_type')
log.addHandler(handler)

fmt_log = MarqueeFormatter('theherk.testapp')
handler.setFormatter(fmt_log)

log.info('Hello. This is dog.')

fmt_event = MarqueeEventFormatter(event_type='theherk.testevent', source='theherk.testapp')
handler.setFormatter(fmt_event)

log.error(
    json.dumps(
        {
            'user':'jeffrey',
            'other':'stuff'
        }
    )
)
