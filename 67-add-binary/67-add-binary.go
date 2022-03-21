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
    mapper := map[string]int{"0": 0, "1": 1}
    
    for i := 0; i < len(min); i++ {
        sum = pre + mapper[string(min[len(min)-i-1])] + mapper[string(max[len(max)-i-1])]
        pre = sum / 2
        if sum % 2 == 0 {
            answer = "0" + answer
        } else {
            answer = "1" + answer
        }
    }
    
    for i := len(min); i < len(max); i++ {
        sum = pre + mapper[string(max[len(max)-i-1])]
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
