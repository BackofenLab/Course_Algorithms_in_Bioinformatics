from prakt.gt import GotohBase


@GotohBase.register
class Gotoh(GotohBase):
    """Document me!"""

    def run(self,
            seq1_fasta_fn,
            seq2_fasta_fn,
            subst_matrix_fn,
            factor_gap_alpha,
            factor_gap_beta,
            complete_traceback):
            """Document me!"""
            # return some dummy results
            return ("idA",
                    "FancySequenceA",
                    "idB",
                    "FancysequenceB",
                    1000,
                    [("Fancy_SequenceA_", "Fancys_equence_B")])
