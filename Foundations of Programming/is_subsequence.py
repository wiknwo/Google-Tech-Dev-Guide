def is_subsequence(subsequence, sequence, subsequence_length, sequence_length):
    # Base Cases
    if subsequence_length == 0:
        return True

    if sequence_length == 0:
        return False

    # Inductive Steps

    # Last characters matching
    if subsequence[subsequence_length - 1] == sequence[sequence_length - 1]:
        return is_subsequence(subsequence, sequence, subsequence_length - 1, sequence_length - 1)

    # Last characters not matching
    return is_subsequence(subsequence, sequence, subsequence_length, sequence_length - 1)
