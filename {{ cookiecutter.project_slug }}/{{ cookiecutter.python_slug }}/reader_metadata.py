#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import bioio_base.reader_metadata

###############################################################################


class ReaderMetadata(bioio_base.reader_metadata.ReaderMetadata):
    @staticmethod
    def get_supported_extensions() -> List[str]:
        """
        Return a list of file extensions this plugin supports reading.
        """
        raise NotImplementedError()
        # return ["ext", "extn"]

    @staticmethod
    def get_reader() -> bioio_base.reader.Reader:
        from .reader import Reader

        return Reader
