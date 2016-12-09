from prakt.nw3 import NeedlemanWunsch3Base


@NeedlemanWunsch3Base.register
class NeedlemanWunsch3(NeedlemanWunsch3Base):
    """Document me!"""

    def run(self,
            seq_fasta_fn,
            subst_matrix_fn,
            cost_gap_open,
            complete_traceback):
            """Document me!"""
            # return some dummy results
            return ("idA",
                    "FancySequenceA",
                    "idB",
                    "FancysequenceB",
                    "idC",
                    "FancySequenceC",
                    1000,
                    [("Fancy_SequenceA__",
                      "Fancys_equence_B_",
                      "Fancy_Sequence__C")])

if __name__ == '__main__':
    # run Needleman-Wunsch with some parameters
    nw3 = NeedlemanWunsch3()
    nw3.run(
        "data/threeseqs.fa",
        "data/blosum62.txt",
        5,
        True)
