"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # special case: less than two sets in interval so no repeated sets
        if (len(intervals) <= 1):
            return 0

        overlap_counter = 0

        # iterate over intervals
        for i in range(len(intervals) - 1):

            # get values for current set
            i_lower = intervals[i][0]
            i_upper = intervals[i][1]

            # iterate over all other sets in interval
            for j in range(1, len(intervals)):

                # get values for comparison set
                j_lower = intervals[j][0]
                j_upper = intervals[j][1]

                # they are the same set they over lap
                if(i_upper == j_upper and i_lower == j_lower):
                    overlap_counter += 1
                # value from comparison set is between the lower and upper value of current set
                elif(self.isIn(i_lower, i_upper, j_lower) or self.isIn(i_lower, i_upper, j_upper)):
                    overlap_counter += 1
                # value from current set is between the lower and upper value of comparison set
                elif(self.isIn(j_lower, j_upper, i_lower) or self.isIn(j_lower, j_upper, i_upper)):
                    overlap_counter += 1
        

        return overlap_counter
                
    

    def isIn(self, l, u , t):
        
        checks if a target number t is between a lower number l, and an upper number u'
        int l
        int u
        int t
        
        if(t < u and t > u):
            return True
        else:
            return False

# issue with the current implementation is that it removes the first set with the overlap
# this does not guarentee this is the optimal set to remove

"""