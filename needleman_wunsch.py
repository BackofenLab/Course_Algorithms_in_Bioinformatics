from prakt.nw import NeedlemanWunschBase


@NeedlemanWunschBase.register
class NeedlemanWunsch(NeedlemanWunschBase):

    def run(self, seq1_fasta_fn, seq2_fasta_fn, subst_matrix_fn, cost_gap_open, complete_traceback):
            print(seq1_fasta_fn)
            print(seq2_fasta_fn)

if __name__ == '__main__':
    print(issubclass(NeedlemanWunsch, NeedlemanWunschBase))
    print(isinstance(NeedlemanWunsch(), NeedlemanWunschBase))
    nw = NeedlemanWunsch()
    nw.run("a", "b", "c", "d", True)
