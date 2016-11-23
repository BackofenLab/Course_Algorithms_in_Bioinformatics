from prakt.nw import NeedlemanWunschBase


@NeedlemanWunschBase.register
class NeedlemanWunsch(NeedlemanWunschBase):

    def run(self, seq1_fasta_fn, seq2_fasta_fn, subst_matrix_fn, cost_gap_open, complete_traceback):
            return ("idA",
                    "FancySequenceA",
                    "idB",
                    "FancysequenceB",
                    1000,
                    [("Fancy_SequenceA_", "Fancys_equence_B")])

if __name__ == '__main__':
    print(issubclass(NeedlemanWunsch, NeedlemanWunschBase))
    print(isinstance(NeedlemanWunsch(), NeedlemanWunschBase))
    nw = NeedlemanWunsch()
    nw.run(
        "data/sequence1.fa",
        "data/sequence2.fa",
        "data/blosum62.txt",
        5,
        True)
