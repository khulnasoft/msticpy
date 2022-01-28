# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""Deprecated placeholder for timeline_pd_accessor.py."""
import warnings
from .._version import VERSION

__version__ = VERSION
__author__ = "Pete Bryan"


# flake8: noqa: F403, F401
# pylint: disable=wildcard-import, unused-wildcard-import, unused-import
from ..vis.timeline_pd_accessor import *

WARN_MSSG = (
    "This module has moved to msticpy.vis.timeline_pd_accessor\n"
    + "Please change your import to reflect this new location."
)
warnings.warn(WARN_MSSG, category=DeprecationWarning)
