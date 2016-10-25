"""marquee logging formatter."""
import json
from logging import Formatter


class MarqueeFormatter(Formatter):
    def __init__(self, source=None, *args, **kwargs):
        """marquee logging formatter.

        Args:
            source (str): application from which your are logging
        """
        self.source = source if source is not None else __name__
        super(MarqueeFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        """Overridden format method.

        This will create a json object containing data for the CloudWatch Event.
        """
        return json.dumps({
            'created': self.formatTime(record),
            'level': record.levelname,
            'level_number': record.levelno,
            'message': super(MarqueeFormatter, self).format(record)
        })

class MarqueeEventFormatter(Formatter):
    def __init__(self, event_type=None, source=None, *args, **kwargs):
        """marquee event formatter.
        """
        self.source = source if source is not None else __name__
        self.event_type = event_type if event_type else self.source
        super(MarqueeEventFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        """Overridden format method.
        This will create a json object containing data for the CloudWatch Event.
        """
        return json.dumps({
            'created': self.formatTime(record),
            'event-type': self.event_type,
            'event': super(MarqueeEventFormatter, self).format(record)
        })
