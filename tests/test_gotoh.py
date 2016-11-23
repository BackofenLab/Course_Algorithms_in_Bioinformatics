from gotoh import Gotoh


def test_example():
    """Test if run function can be called."""
    gt = Gotoh()
    result = gt.run("data/sequence1.fa",
           "data/sequence2.fa",
           "data/blosum62.txt",
           5,
           20,
           False)