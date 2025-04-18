def gen_arithmetic_sequence(first, last, diff):
    """產生等差數列"""
    seq = []
    current = first
    while current <= last:
        seq.append(current)
        current += diff
    return seq
