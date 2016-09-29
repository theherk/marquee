"""marquee logging handler."""
from logging import Handler

import boto3

from marquee.formatter import MarqueeFormatter


class CloudWatchEventsHandler(Handler):
    def emit(self, record):
        """Overridden emit method.

        This will emit the log message to CloudWatch Events. Permissions
        and target account all set according to normal boto resolution.
        """
        client = boto3.client('events')
        source = self.formatter.source if isinstance(self.formatter, MarqueeFormatter) else __name__
        return client.put_events(
            Entries=[
                {
                    'Time': self.formatter.formatTime(record),
                    'Source': source,
                    'DetailType': 'marquee',
                    'Detail': self.format(record)
                }
            ]
        )
