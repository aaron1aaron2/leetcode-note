class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def Counter(s):
            dt = {}
            for i in s:
                if i in dt:
                    dt[i] += 1
                else:
                    dt[i] = 1

            return  dt

        ct_dt = {} # {group: count_dict}
        str_dt = {} # {length:{group: str}}

        for i in strs:
            l = len(i)
            ct = Counter(i)
            if l not in str_dt:
                str_dt[l] = {i:[i]}
                ct_dt[i] = ct
            else:
                match_ = False
                for gp_key in str_dt[l].keys():
                    if ct == ct_dt[gp_key]:
                        str_dt[l][gp_key].append(i)
                        match_ = True
                        break

                if not match_:
                    str_dt[l][i] = [i]
                    ct_dt[i] = ct

        result = []
        for l in str_dt.keys():
            for gp in str_dt[l].keys():
                result.append(str_dt[l][gp])
            
        return result
