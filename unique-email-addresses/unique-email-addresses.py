class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        for i in emails:            
            local = ""
            for j in i:
                if j == "+" or j == "@":
                    break
                if j == ".":
                    continue
                local = local + j
                
            domain = ""
            for k in reversed(i):
                if k == "@":
                    break
                domain = k + domain
                
            uniqueEmails.add(local + "@" + domain)
            
        return len(uniqueEmails)