def maxScore(cardPoints, k):
    n = len(cardPoints)
    current_sum = sum(cardPoints[:k])
    max_sum = current_sum
    
    for i in range(1, k + 1):
        current_sum += cardPoints[-i] - cardPoints[k - i]
        max_sum = max(max_sum, current_sum)
        
    return max_sum

#input is hardcoded! Change for different use cases
cardPoints = [9,7,7,9,7,7,9] 
k = 7
print(maxScore(cardPoints, k))