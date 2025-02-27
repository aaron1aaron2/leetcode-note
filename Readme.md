# leetcode practise

<p align="center">
<img src="./img/roadmap.png" alt="Alt Text" style="width:80%; height:auto;">
</p>

_roadmap from https://neetcode.io/roadmap_

## Topic
### Arrays & Hashing 

### Two Pointers

### Stack

### Binary Search

### Sliding Window

### Linked List

### Trees

### Tries

### Backtracking

### Heap / Priority Queue

### Graphs

### Advanced Graphs

### 1-D DP

### 2-D DP

### Intervals

### Greedy

### Bit Manipulation

### Math & Geometry



### Daily
- 1352 - Product of the Last K Numbers [[code](./code/1352-2.%20Product%20of%20the%20Last%20K%20Numbers.py)] [[link](https://leetcode.com/problems/product-of-the-last-k-numbers/)]
  - `Medium`、`O(nlogm)`
  - Tags: `Array`、`Math`、`Design`、`Data Stream`、`Prefix Sum`
  - Note: 在需要多次查詢區間資料和或是相乘的情況下，透過前綴和(Prefix Sum)或是前綴乘(Prefix product)的小技巧，可以有效提高運行效率。

- ★ 2342 - Max Sum of a Pair With Equal Sum of Digits [[code](./code/2342-3.%20Max%20Sum%20of%20a%20Pair%20With%20Equal%20Sum%20of%20Digits.py)] [[link](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/)]
  - `Medium`、` implement both GetProduct and Add to work in O(1) time complexity`
  - Tags: `Array`、`Hash Table`、`Sorting`、`Heap (Priority Queue)`

- ★ 2375 - Construct Smallest Number From DI String  [[code](./code/2375-2.%20Construct%20Smallest%20Number%20From%20DI%20String.py)] [[link](https://leetcode.com/problems/construct-smallest-number-from-di-string/)]
  - `Medium`、`O(n)`
  - Tags: `String`、`Backtracking`、`Stack`、`Greedy`、`recursion`
  - Note: 在一些限制下，暴力解也是一種方法。但是可以透過一些技巧，進一步減少暴力解的時間複雜度。這題遞迴和 stack 的方式不直觀需要多看幾次。
  - <details><summary>more</summary><b>
  
    #### approch1: Brute Force | O(n!⋅n^2)
    ```python
    # Because the length is not very long in terms of conditions, you can use the method of trying to use brute force search to solve it
    class Solution:
        def smallestNumber(self, pattern: str) -> str:
            length = len(pattern) # <= 8
            from itertools import permutations
            all_results = permutations(range(1, 10), length+1) # get all permutations using python built-in itertools tool
    
            # By default, the order is sorted by number size, so we can directly compare from small to large in order, without having to sort it anymore
            for seq in all_results:
                seq_str = ''.join([str(i) for i in seq])
                result = self.check_pattern(seq, pattern)
    
                if result:
                    return seq_str
        
        def check_pattern(self, seq: str, pattern: str) -> bool:
            # if part od seq not match return false
            for idx, pat in enumerate(pattern):
                if pat == 'I':
                    if seq[idx] > seq[idx+1]:
                        return False
                else:
                    if seq[idx] < seq[idx+1]:
                        return False
            
            # when whole seq is pass, return true
            return True
    ```

    #### approch2: Brute Force via Recursion | O(n)
    ```python
    # Regulated Brute Force via Recursion | solution of editorial
    # The print in the code is just to help understand the state of recursion 
    class Solution:
        def smallestNumber(self, pattern: str) -> str:
            self.result = []
    
            # Start building the sequence by calling the helper function
            self.build_sequence(0, 0, pattern)
            # Reverse the final result
            return "".join(self.result[::-1])
    
        # Recursively build the sequence
        def build_sequence(
            self, current_index: int, current_count: int, pattern: str
        ) -> int:
            if current_index != len(pattern):
                if pattern[current_index] == "I":
                    # If 'I', increment the count and move to the next index
                    print('I', current_index, '|', current_count)
                    self.build_sequence(current_index + 1, current_index + 1, pattern)
                else:
                    # If 'D', keep the count and move to the next index
                    print('D', current_index, '|', current_count)
                    current_count = self.build_sequence(
                        current_index + 1, current_count, pattern
                    )
            
            print(current_index, '|', current_count, 'D')
            self.result.append(str(current_count + 1))
            print('append', current_count + 1)
    
            # Return the next count for the sequence
            return current_count + 1
    ```
 
    ##### test case -> pattern = "IIIDIDDD"
    ```
    I 0 | 0
    I 1 | 1
    I 2 | 2
    D 3 | 3
    I 4 | 3
    D 5 | 5
    D 6 | 5
    D 7 | 5
    8 | 5 D
    append 6
    7 | 6 D
    append 7
    6 | 7 D
    append 8
    5 | 8 D
    append 9
    4 | 3 D
    append 4
    3 | 4 D
    append 5
    2 | 2 D
    append 3
    1 | 1 D
    append 2
    0 | 0 D
    append 1
    ```

    #### approch3: Stack | O(n)
    ```python
    class Solution:
        def smallestNumber(self, pattern: str) -> str:
            result = []
            num_stack = []
    
            # Iterate through the pattern
            for index in range(len(pattern) + 1):
                print("-"*10, f'iter{index}', "-"*10)
                # Push the next number onto the stack
                num_stack.append(index + 1)
                print('stack:', num_stack)
    
                # If 'I' is encountered or we reach the end, pop all stack elements
                if index == len(pattern) or pattern[index] == "I":
                    while num_stack:
                        result.append(str(num_stack.pop()))
                        print('result:', result)
    
    
            return "".join(result)
    ```

    ##### test case -> pattern = "IIIDIDDD"
    ```
    ---------- iter0 ----------
    stack: [1]
    result: ['1']
    ---------- iter1 ----------
    stack: [2]
    result: ['1', '2']
    ---------- iter2 ----------
    stack: [3]
    result: ['1', '2', '3']
    ---------- iter3 ----------
    stack: [4]
    ---------- iter4 ----------
    stack: [4, 5]
    result: ['1', '2', '3', '5']
    result: ['1', '2', '3', '5', '4']
    ---------- iter5 ----------
    stack: [6]
    ---------- iter6 ----------
    stack: [6, 7]
    ---------- iter7 ----------
    stack: [6, 7, 8]
    ---------- iter8 ----------
    stack: [6, 7, 8, 9]
    result: ['1', '2', '3', '5', '4', '9']
    result: ['1', '2', '3', '5', '4', '9', '8']
    result: ['1', '2', '3', '5', '4', '9', '8', '7']
    result: ['1', '2', '3', '5', '4', '9', '8', '7', '6']
    ```
    
    </b></details>

- 3066 - Minimum Operations to Exceed Threshold Value II  [[code](./code/3066-2.%20Minimum%20Operations%20to%20Exceed%20Threshold%20Value%20II.py)] [[link](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii)]
  - `Medium`、`O(nlogm)` 
  - Tags: `Array`、`Heap (Priority Queue)`、`Simulation`

- 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray [[code](./code/3105.%20Longest%20Strictly%20Increasing%20or%20Strictly%20Decreasing%20Subarray.py)] [[link](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray)]
  - `Easy`、`O(1)`
  - Tags: `Array`

## Reference
- [Neetcode-150-and-Blind-75](https://github.com/envico801/Neetcode-150-and-Blind-75/tree/main)
- [Neetcode150](https://neetcode.io/practice?tab=neetcode150)
