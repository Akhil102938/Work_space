from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Sorted characters create the same key for anagrams
            key = "".join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
