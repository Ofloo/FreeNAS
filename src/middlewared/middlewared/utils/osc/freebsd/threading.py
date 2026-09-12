# -*- coding=utf-8 -*-
import logging

try:
    from bsd.threading import set_thread_name
except ImportError:
    def set_thread_name(name):
        pass

logger = logging.getLogger(__name__)

__all__ = ["set_thread_name"]
