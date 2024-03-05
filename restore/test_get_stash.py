# Copyright (c) The stash contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from get_stash import ensure_json, gh_api, jq


class TestGetStash(unittest.TestCase):
    def test_jq(self):
        self.assertEqual(jq('{"a": 1}', ".a", ["-j"]).stdout, "1")

    def test_jq_file(self):
        self.assertEqual(jq("test.json", ".a").stdout, "1\n")

    def test_jq_error(self):
        with self.assertRaises(ValueError):
            jq("not_found.json", ".a")

    def test_gh_api(self):
        self.assertEqual(
            gh_api("rate_limit", options=["-q", ".resources.core.limit"]).stdout,
            "5000\n",
        )

    def test_ensure_json(self):
        # use the actual response from gh_api to guard against changes in the API
        res = gh_api("rate_limit", options=["-q", ".resources.cre.limit"])
        count = ensure_json(res.stdout)
        self.assertIsNone(count)

if __name__ == "__main__":
    unittest.main()
