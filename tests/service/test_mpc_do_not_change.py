#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

#############################################################################
# This test file is a short-term to freeze the file change during migration.
# After migration completed, we shall delete this ut test
# TODO: T137598681 clean up FBPCS mpc related files after migration complete
#############################################################################
import hashlib
import inspect
import unittest

from fbpcp.entity.mpc_game_config import MPCGameConfig
from fbpcp.entity.mpc_instance import MPCInstance
from fbpcp.repository.mpc_game_repository import MPCGameRepository
from fbpcp.repository.mpc_instance import MPCInstanceRepository

from fbpcp.service.mpc import MPCService
from fbpcp.service.mpc_game import MPCGameService

from .test_mpc import TestMPCService
from .test_mpc_game import TestMPCGameService

NO_CHANGE_FILES = (
    {
        "cls": MPCService,
        "file_md5": "35dbe2a73b1016d6d631b03abc612929",
    },
    {
        "cls": TestMPCService,
        "file_md5": "6a1c7a74f28d164e113b68dbcab29962",
    },
    {
        "cls": MPCGameService,
        "file_md5": "36a2142e36759e382855e970f12c7403",
    },
    {
        "cls": TestMPCGameService,
        "file_md5": "e1e4517471ff5630a7a7dc5db645ed5f",
    },
    {
        "cls": MPCGameConfig,
        "file_md5": "39326c1de0bb8795313ce84560d25c97",
    },
    {
        "cls": MPCGameRepository,
        "file_md5": "d2d09421e3ab8c612a2208d7a0269996",
    },
    {
        "cls": MPCInstance,
        "file_md5": "4a52cc896d438cb8900649265eb46b71",
    },
    {
        "cls": MPCInstanceRepository,
        "file_md5": "251b27ef762c7421a43fe1e8062ce86b",
    },
)


class TestMPCDontChange(unittest.TestCase):
    def test_mpc_service_no_change(self):
        for no_change_file in NO_CHANGE_FILES:
            cls_name = no_change_file["cls"]
            file_name = inspect.getfile(cls_name)
            self.assertEqual(
                no_change_file["file_md5"],
                self.gen_file_md5(file_name),
                msg=f"assertion on file: {file_name}",
            )

    def gen_file_md5(self, file_name):
        with open(file_name, "rb") as file_to_check:
            data = file_to_check.read()
            # pipe contents of the file through
            return hashlib.md5(data).hexdigest()
