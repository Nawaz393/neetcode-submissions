class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        encoded_string=''
        for s in strs:
            encoded_string+=str(len(s))
            encoded_string+='#'
            encoded_string+=s

        return encoded_string



    def decode(self, s: str) -> List[str]:
            if not s:
                return []
            decoded=[]
            j=i=0
            while i<len(s):
                while s[j]!='#':
                    j+=1
                str_len=int(s[i:j])
                i=j+1
                j=i+str_len
                decoded.append(s[i:j])
                i=j
            return decoded


            

