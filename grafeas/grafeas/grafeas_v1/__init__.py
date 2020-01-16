# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
import sys
import warnings

from grafeas.grafeas_v1 import types
from grafeas.grafeas_v1.gapic import enums
from grafeas.grafeas_v1.gapic import grafeas_client


if sys.version_info[:2] == (2, 7):
    message = (
        "A future version of this library will drop support for Python 2.7."
        "More details about Python 2 support for Google Cloud Client Libraries"
        "can be found at https://cloud.google.com/python/docs/python2-sunset/"
    )
    warnings.warn(message, DeprecationWarning)


class GrafeasClient(grafeas_client.GrafeasClient):
    __doc__ = grafeas_client.GrafeasClient.__doc__
    enums = enums


__all__ = (
    "enums",
    "types",
    "GrafeasClient",
)
