"""marquee logging formatter."""
import json
from logging import Formatter


class MarqueeFormatter(Formatter):
    def __init__(self, source=None, *args, **kwargs):
        """marquee logging formatter.

        Args:
            source (str): application from which your are logging
        """
        self.source = source if source else __name__
        super(MarqueeFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        """Overridden format method.

        This will create a json object containing data for the CloudWatch Event.
        """
        return json.dumps({
            'source': self.source,
            'created': self.formatTime(record),
            'level': record.levelname,
            'level_number': record.levelno,
            'message': record.msg
        })
