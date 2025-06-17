from collections import defaultdict

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # create a dictionary for sorted words
        anagrams = defaultdict(list)
        # loop through and sort the words
        for word in strs:
            # sort the words by each group key
            key = ''.join(sorted(word))
            # add the original word to the dict
            anagrams[key].append(word)

        return list(anagrams.values())
        
