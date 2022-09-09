#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import bioio_types

###############################################################################


class ReaderMetadata(bioio_types.ReaderMetadata):
    @staticmethod
    def get_supported_extensions() -> List[str]:
        return ["ext", "extn"]

    @staticmethod
    def get_reader() -> bioio_types.reader.Reader:
        from .reader import Reader

        return Reader
