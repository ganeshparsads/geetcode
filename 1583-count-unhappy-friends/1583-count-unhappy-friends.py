from collections import defaultdict
class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        
        pair={}
        unhappy=0
        for x,y in pairs:#pair={0:1,1:0,2:3,3:2}
            pair[x]=y
            pair[y]=x
        for k,v in pair.items():#Look at above example and let's assume k=1,v=0 (2nd element in pair)
            kFirstPref=preferences[k][0]# kFirstPref=3,means the 1st pref of 1 is 3
            if kFirstPref==v:#3==0, nopes
                continue
            j=preferences[k].index(v)#preference of v for k j=2
            i=0
            while i<j:#We are checking all the element in preference[k] having greater pref. than v,for i=0
                kIthPref=preferences[k][i]#kIthPref=3,i=0,first pref. of k
                kIthPrefPairing=pair[kIthPref]#kIthPrefPairing=2, with whom the 1st pref of k is paired
                kInd=preferences[kIthPref].index(k)#kInd=0,pref of k(1) for kIthPref i.e 3 here
                kIthPrefPairingInd=preferences[kIthPref].index(kIthPrefPairing)#kIthPrefPairingInd=1,pref of kIthPrefPairing for kIthPref i.e 3 here
                if kInd<kIthPrefPairingInd:
                    unhappy+=1
                    break
                else:
                    i+=1
        return unhappy