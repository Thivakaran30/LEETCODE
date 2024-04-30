class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        
        tot = res = 0
        for i in range(len(gas)):
            tot+=(gas[i]-cost[i])
            if tot < 0:
                tot = 0
                res = i+1
        return res
