"""marquee logging handler."""
from logging import Handler

import boto3

from marquee.formatter import MarqueeFormatter


class CloudWatchEventsHandler(Handler):

    def __init__(self, detail_type=None, *args, **kwargs):
        """Overridden __init__ method.

        Will set detail_type on handler object then invoke Handler __init__
        with any passed in arguments
        """
        self.detail_type = detail_type
        super(CloudWatchEventsHandler, self).__init__(*args, **kwargs)

    def emit(self, record):
        """Overridden emit method.

        This will emit the log message to CloudWatch Events. Permissions
        and target account all set according to normal boto resolution.
        """
        client = boto3.client('events')
        source = self.formatter.source if isinstance(self.formatter, MarqueeFormatter) else __name__
        detail_type = self.detail_type if self.detail_type is not None else 'marquee'
        return client.put_events(
            Entries=[
                {
                    'Time': self.formatter.formatTime(record),
                    'Source': source,
                    'DetailType': detail_type,
                    'Detail': self.format(record)
                }
            ]
        )
