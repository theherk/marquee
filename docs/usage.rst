=====
Usage
=====

Handler
-------

To use the handler, simply add it to you log::

    import logging

    from marquee.formatter import MarqueeFormatter
    from marquee.handler import CloudWatchEventsHandler

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    handler = CloudWatchEventsHandler()
    log.addHandler(handler)

Formatter
---------

To use the formatter, which is optional, add it to your handler. If you don't use this formatter, `__name__` will be used for the source in the handler. If you do, you can pass `source` too the handler along with any other formatter arguments. Then, this will be included in the CloudWatch Event.

To add the formatter to the handler::

    fmt = MarqueeFormatter('theherk.testapp')
    handler.setFormatter(fmt)
