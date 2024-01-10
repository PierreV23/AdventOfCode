
Bound = int | float
LowerBound = Bound
UpperBound = Bound

class Range:
    start: LowerBound
    end: UpperBound
    def __init__(self, start: LowerBound, end: UpperBound):
        if (isinstance(start, float) and start != float('-inf')) or (isinstance(end, float) and end != float('inf')):
            raise Exception(f"Invalid value for either {start=}, {end=}")
        self.start = start
        self.end = end


# Range(...) & Range(...) -> Range(...) 
#   whatever overlaps -> overlap
# Range(...) ^ Range(...) -> Range(...) | None, Range(...) | None
#   whatever doesnt overlap -> left, right
# Range(...) | Range(...) -> Range(...) | None
#   two ranges become one, unless they didnt overlap, then it returns none
