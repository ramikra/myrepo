## sequence.py ##

class Sequence:
# This method is the initializer, it is called when creating (instantiating) an 
# object (instance) of this class.
    def __init__(self, bases):
    # store the bases as an attribute.
        self.bases = bases

# 1. Define a method on your class which returns the number of DNA bases (i.e. characters)
# in the sequence.

    def length(self):
        result = len(self.bases)
        return result

# 2. Define a is_dna() method on your class, which validates whether the all the characters
# are valid DNA bases: A,T, C or G. It should return True or False. If the sequence has zero
# length, it should return False.

    def is_dna(self):
        if len(self.bases) == 0:
            return False
        for i in self.bases:
            if i == 'A' or i == 'T' or i == 'C' or i == 'G':
                result = True
            else:
                result = False
                break
        return result

# 3. Define a method which returns the complement of the Sequence as a new Sequence
# instance. (i.e. every A becomes a T, and every C a G – and vice-versa). Do not reverse
# the complement sequence.

    def complement(self):
            result = ''
            for i in self.bases:
                if i == 'A':
                    result += 'T'
                elif i == 'T':
                    result += 'A'
                elif i == 'C':
                    result += 'G'
                elif i == 'G':
                    result += 'C'
            return result

# 4. Create a method that finds the first pair of non-matching bases, when comparing with
# another Sequence instance. Return the zero-based index of the first non-matching base.
# Return -1 if the sequences are identical (or empty). You can assume (or assert) the
# sequences have the same length. e.g. comparing sequences ACGTGCG and ACGTTCG
# returns 4.

    def compare(self, seq2):
        if self.bases == seq2.bases:
            return -1
        else:
            for i in range(len(self.bases)):
                if self.bases[i] != seq2.bases[i]:
                    return i


