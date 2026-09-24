class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            # Recalculate sum on every iteration
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                # 1-indexed return. Change to [i, j] if 0-indexed is required.
                return [i + 1, j + 1]
            elif current_sum > target:
                j -= 1
            else:
                i += 1
                
        return []