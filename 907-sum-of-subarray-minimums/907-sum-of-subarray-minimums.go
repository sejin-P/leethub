func sumSubarrayMins(arr []int) int {
    if len(arr) == 1 {
        return arr[0]
    }
    
    length := len(arr)
    prev := sumSubarrayMins(arr[:length-1])
    
    minNum := arr[length-1]
    for idx, _ := range arr[:length] {
        minNum = min(minNum, arr[length-1-idx])
        prev += minNum
    }
    
    return prev%(int(math.Pow10(9))+7)
}

func min(a int, b int) int {
    if a > b {
        return b
    }
    return a
}
