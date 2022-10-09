"""Test bitext.py."""
import sys
import pytest
from omegaconf.dictconfig import DictConfig
sys.path.append("../src/")

import methods.ibm2 as ibm2
from bitexts import Bitext, Bitexts


@pytest.fixture(scope="module")
def query_config():
    return DictConfig({
        "poem": 1,
        "word_1": "BG-01-1630-01-0100",
        "word_2": "BG-01-1770-01-0300",
        "translator_1": "金子",
        "translator_2": "片桐",
    })


@pytest.fixture(scope="module")
def config():
    with open("../cache/bitexts.csv") as fp:
        row = fp.readlines()[57]
    fields = row.strip().split(",")
    return fields


@pytest.fixture(scope="module")
def model():
    model_1 = ibm2.load("../model/ibm2_fwd.model")
    model_2 = ibm2.load("../model/ibm2_bwd.model")
    return model_1, model_2


@pytest.fixture(scope="module")
def translators():
    return [
        "kaneko", "katagiri", "kojimaarai", "komachiya", "kubota", "kyusojin",
        "matsuda", "okumura", "ozawa", "takeoka"
    ]


def test_bitext(config, query_config, model):
    """Test bitext class."""
    bitext_ = Bitext(*config, *model)
    # print(bitext_.source, bitext_.target)
    assert len(bitext_.alignment_source2target) == len(bitext_.source)
    assert len(bitext_.alignment_target2source) == len(bitext_.target)
    list(bitext_.proper_alignment_idx())
    list(bitext_.proper_alignment())
    list(bitext_.improper_alignment_idx())
    list(bitext_.improper_alignment())
    list(bitext_.query_improper_alignment_by_token(query_config.word_1))
    list(bitext_.query_proper_alignment_by_token(token=query_config.word_1))
    bitext_.alignment_table_src2tar()
    bitext_.alignment_table_tar2src()


def test_bitexts(config, query_config, translators):
    """Test bitexts class."""
    bitexts_ = Bitexts(translators)
    bitexts_[0]
    list(bitexts_.query_by_poem("1"))
    list(
        bitexts_.query_bitext_by_word(query_config.word_1,
                                      query_config.word_2))
    list(
        bitexts_.query_bitext_by_translator(query_config.translator_1,
                                            query_config.translator_2))
    list(
        bitexts_.query_proper_alignment_by_word(query_config.word_1,
                                                query_config.word_2))
    list(
        bitexts_.query_improper_alignment_by_word(query_config.word_1,
                                                  query_config.word_2))


if __name__ == "__main__":
    pytest.main(["test_bitexts.py", "-s"])
