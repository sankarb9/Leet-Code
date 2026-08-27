class Solution(object):
    def frequencySort(self, s):
        from collections import Counter
        temp=[]
        count=Counter(s)
        for ch,freq in count.most_common():
            temp.append(ch*freq)
        return ''.join(temp)