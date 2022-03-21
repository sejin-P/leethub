func addBinary(a string, b string) string {
    if len(a) > len(b) {
        return add(b, a)
    }
    
    return add(a, b)
}

func add(min string, max string) string {
    answer := ""
    pre := 0
    sum := 0
    mapper := map[uint8]int{48: 0, 49: 1}
    
    for i := 0; i < len(min); i++ {
        sum = pre + mapper[min[len(min)-i-1]] + mapper[max[len(max)-i-1]]
        pre = sum / 2
        if sum % 2 == 0 {
            answer = "0" + answer
        } else {
            answer = "1" + answer
        }
    }
    
    for i := len(min); i < len(max); i++ {
        sum = pre + mapper[max[len(max)-i-1]]
        pre = sum / 2
        if sum % 2 == 0 {
            answer = "0" + answer
        } else {
            answer = "1" + answer
        }
    }
    
    if pre == 1{
        answer = "1" + answer
    }
    
    return answer
}
