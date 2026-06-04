class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        seen = {} # sorted_str: idxes
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in seen:
                seen[sorted_word].append(i)
            else:
                seen[sorted_word] = [i] 
        #[0,3], [1,2]
        ans = []    
        for j in seen.values():
            to_append = []
            for k in j:
                to_append.append(strs[k])
            ans.append(to_append)
        return ans
