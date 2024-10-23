class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "" #빈 리스트 입력 시 빈 문자열 반환
        
        short_str = min(strs, key=len) # 사전순이 아닌 문자열 길이로 최소값 찾기
        for i in range(len(short_str)): # 가장 짧은 문자열 기준으로
            for s in strs: # 기존 strs 리스트 내 요소들과 비교
                if s[i] != short_str[i]: # 더이상 일치하는 문자가 없으면
                    return short_str[:i] # i-1번째까지 문자열 출력
        
        return short_str #모든 문자열이 공통 접두어일 경우