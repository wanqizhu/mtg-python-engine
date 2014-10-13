def intersection(dict1, dict2, combiner):
    """Gives the intersection of dict1 and dict2 with each key k mapping to
    combiner(k, dict1[k], dict2[k])"""
    keys1 = set(dict1.keys())
    keys2 = set(dict1.keys())
    return {k:combiner(k, dict1[k], dict2[k]) for k in keys1 & keys2}

def union(dict1, dict2, combiner):
    """Gives the union of dict1 and dict2, such that if k is in both, then
    result[k]=combiner(k, dict1[k], dict2[k]). combiner should be commutative
    with regards to the last two variables"""
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    result = dict1.copy().update(dict2.copy())
    result.update(intersection(dict1, dict2, combiner))
    return result
    
class ContradictionError(Exception):
    pass

def normalize_intervals(bounds):
    """Normalizes a list of integer intervals (represented as (min, max)
    pairs)"""
    sorted_bounds = sorted(bounds)
    normalized = [bounds[0]]
    for (low, high) in bounds:
        if low > high:
            continue
        test_low, test_high = normalized.pop(-1)
        if low < test_high:
            if test_high < high:
                normalized.append((test_low, high))
            else:
                normalized.append((test_low, test_high))
        else:
            normalized.extend([(test_low, test_high), (low, high)])
    return normalized
    
def interval_contains(bounds, element):
    low, high = bounds
    return low <= element <= high
    
class IntervalSet(object):
    def __init__(self, bounds):
        """Describes a set of integer intervals, for determining membership.
        bounds should be a list of pairs, representing low and high bounds
        of closed intervals. Floating point +/- infinty should be passed
        for unbounded upper and lower bounds, respectively."""
        self.bounds = normalize_intervals(bounds)
        if not self.bounds:
            raise ContradictionError()
        
    def __in__(self, element):
        return any(interval_contains(interval, element) for interval in bounds)
        
    def __or__(self, other):
        try:
            return IntervalSet(self.bounds + other.bounds)
        except AttributeError:
            raise NotImplementedError("Cannot operate IntervalSet with {}".format(other.__class__))
            
    def __invert__(self):
        inf = float("infinity")
        new_bounds = []
        if self.bounds[0][0] > -inf:
            new_bounds.append((-inf, self.bounds[0][0]-1))
        for i in range(len(self.bounds)-1):
            new_bounds.append((self.bounds[i][1]+1, self.bounds[i+1][0]-1))
        if self.bounds[-1][1] < inf:
            new_bounds.append((self.bounds[-1][1]+1, inf))
        return IntervalSet(new_bounds)
        
    def __and__(self, other):
        try:
            return ~((~self) | (~other))
        except AttributeError:
            raise NotImplementedError("Cannot operate IntervalSet with {}".format(other.__class__))
            
def matches(game_obj, key, value, match_fun):
    try:
        return match_fun(game_obj, key, value)
    except AttributeError:
        raise ValueError("The passed object is not of the kind that can be matched by this filter")
    
class Filter(object):
    def __init__(self, conditions=None):
        if conditions is None:
            conditions = {}
        self.conditions = conditions
        
    def matches(self, game_obj):
        return all(matches(game_obj, key, value, match_funs[key]) for (key, value) in self.conditions.items())
        
    def __or__(self, other):
        try:
            return Filter(union(self.conditions, other.conditions, lambda a,b: a|b))
        except AttributeError:
            raise ValueError("Cannot operate Filter with {}".format(other.__class__))
        
    def __and__(self, other):
        try:
            return Filter(intersection(self.conditions, other.conditions, lambda a,b: a&b))
        except Contradiction:
            return EmptyFilter()
        except AttributeError:
            raise ValueError("Cannot operate Filter with {}".format(other.__class__))
        
    def __call__(self, game_obj):
        return self.matches(game_obj)
        
class EmptyFilter(Filter):
    def matches(self, game_obj):
        return False