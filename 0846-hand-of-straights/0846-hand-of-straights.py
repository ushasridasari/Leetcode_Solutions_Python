class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #Check whether cards can be divided evenly
        if len(hand) % groupSize:
            #if not return false
            return False

        #Count how many copies of each card exist
        count = Counter(hand)
        #Check every card, because any card mmight become the begining of the card
        for num in hand:
            #Assume current card is the start
            start = num
            #Check whether a smaller card exist
            while count[start -1]:
                #Move left if smaller card exists
                start -= 1
            #Keep making groups beginning at start
            while start <= num:
                #Do we still have this card
                while count[start]:
                    #Build one group.
                    for i in range(start, start + groupSize):
                        #Do we have this card left?
                        if not count[i]:
                            return False
                        count[i] -= 1
                #Move to next group.
                start += 1
        return True

 #TC: O(n)
 #SC: O(n)
        