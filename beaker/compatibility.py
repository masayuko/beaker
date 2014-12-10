# -*- coding: utf-8 -*-
import sys
py3k = getattr(sys, 'py3kwarning', False) or sys.version_info >= (3, 0)

if py3k:
    string_types = (str,)
    def iteritems(d, **kw):
        return iter(d.items(**kw))
else:
    string_types = basestring
    def iteritems(d, **kw):
        return d.iteritems(**kw)
