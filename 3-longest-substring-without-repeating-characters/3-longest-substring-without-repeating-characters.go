func lengthOfLongestSubstring(s string) int {
    letterDict := map[uint8]int{}
    result := 0
    start := 0
    for i := 0; i < len(s); i++ {
        idx, ok := letterDict[s[i]]
        if !ok || idx < start {
            if i-start+1 > result {
                result += 1
            }
        } else {
            start = idx + 1
        }
        
        letterDict[s[i]] = i
    }
    
    return result
}