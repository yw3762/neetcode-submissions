class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n_hand = len(hand)
        if n_hand % groupSize != 0:
            return False
        
        count = dict(Counter(hand))
        while count:
            first = sorted(count)[0]
            grpRemainings = groupSize
            while grpRemainings > 0:
                if first not in count.keys():
                    return False
                count[first] -= 1
                if count[first] == 0:
                    count.pop(first)
                first += 1
                grpRemainings -= 1
                
        
        return True    
                