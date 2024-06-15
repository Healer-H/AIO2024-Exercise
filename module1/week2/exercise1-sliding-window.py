from collections import deque

def max_sliding_window(arr, k):
    result = []
    if k >= len(arr):
        return [max(arr)]
    
    for i in range(len(arr) - k + 1):
        min_val = max(arr[i:i+k])
        result.append(min_val)
    
    return result


def max_sliding_window_optimized(arr, k):
    if k >= len(arr):
        return [max(arr)]
    result = []
    sliding_window_index = deque()

    for index, val in enumerate(arr):
        while sliding_window_index and sliding_window_index[0] <= max(0, index - k):
            sliding_window_index.popleft()
        if not sliding_window_index or arr[sliding_window_index[-1]] > val:
           sliding_window_index.append(index)
        elif val > arr[sliding_window_index[-1]]:
            sliding_window_index.clear()
            sliding_window_index.append(index)
        if index >= k - 1:
            result.append(arr[sliding_window_index[0]])    
    return result
  
    
if __name__ == "__main__":
    arr = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] 
    k = 3
    print(max_sliding_window(arr, k))
    print(max_sliding_window_optimized(arr, k))