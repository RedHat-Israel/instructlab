# SPDX-License-Identifier: Apache-2.0

# Standard
from unittest.mock import Mock, patch
import logging

# Third Party
import git
import pytest
import yaml

# First Party
from instructlab import utils

# Local
from .testdata import testdata


class TestUtils:
    """Test collection in instructlab.utils."""

    def test_chunk_docs_wc_exeeds_ctx_window(self):
        with pytest.raises(ValueError) as exc:
            utils.chunk_document(
                documents=testdata.documents,
                chunk_word_count=1000,
                server_ctx_size=1034,
            )
        assert (
            "Given word count (1000) per doc will exceed the server context window size (1034)"
            in str(exc.value)
        )

    def test_chunk_docs_chunk_overlap_error(self):
        with pytest.raises(ValueError) as exc:
            utils.chunk_document(
                documents=testdata.documents,
                chunk_word_count=5,
                server_ctx_size=1034,
            )
        assert (
            "Got a larger chunk overlap (100) than chunk size (24), should be smaller"
            in str(exc.value)
        )

    def test_chunk_docs_long_lines(self):
        chunk_words = 50
        chunks = utils.chunk_document(
            documents=testdata.long_line_documents,
            chunk_word_count=chunk_words,
            server_ctx_size=4096,
        )
        max_tokens = utils.num_tokens_from_words(chunk_words)
        max_chars = utils.num_chars_from_tokens(max_tokens)
        max_chars += utils.DEFAULT_CHUNK_OVERLAP  # add in the chunk overlap
        max_chars += 50  # and a bit extra for some really long words
        for chunk in chunks:
            assert len(chunk) <= max_chars

    @patch(
        "instructlab.utils.git_clone_checkout",
        return_value=Mock(spec=git.Repo, working_dir="tests/testdata/temp_repo"),
    )
    def test_get_git_docs(self, git_clone_checkout):
        with open(
            "tests/testdata/knowledge_valid.yaml", "r", encoding="utf-8"
        ) as qnafile:
            documents = utils.get_git_docs(
                source=yaml.safe_load(qnafile).get("document"),
                skip_checkout=True,
                logger=logging.getLogger("_test_"),
            )
            git_clone_checkout.assert_called_once()
            assert len(documents) == 2
