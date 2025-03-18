# leetcode practise

<p align="center">
<img src="./img/roadmap.png" alt="Alt Text" style="width:80%; height:auto;">
</p>

_roadmap from https://neetcode.io/roadmap_

## Topic
### Arrays & Hashing 
- 1 - Two Sum  [[link](https://leetcode.com/problems/two-sum/)]
  - `Easy`、`O(n) by hash table`
  - Tags: `Array`、`Hash Table`
- 217 - Contains Duplicate [[link](https://leetcode.com/problems/contains-duplicate)]
  - `Easy`
  - Tags:
- 242 - Valid Anagram [[link](https://leetcode.com/problems/valid-anagram)]
  - `Easy`
  - Tags:

### Two Pointers
- 125 - Valid Palindrome [[link](https://leetcode.com/problems/valid-palindrome)]
  - `Easy`、`O(n)`
  - Tags: `Two Pointers`、`String`
  - Note: 換個角度想可以更輕鬆優雅的解決問題，像是在本問題上判斷回文其實可以直接反轉後判斷兩字串是否一致。不一定要透過 pointer 方式去處理

### Sliding Window
- ★ 121 - Best Time to Buy and Sell Stock [[link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)]
  - `Easy`、`O(n)`
  - Tags: `Array`、`Dynamic Programming`
  - Note: 第一次看到這題是想用兩個 pointer 作為買賣點，並在一次迴圈下(O(n))找出最佳買賣時間點和獲利，此作法需要多方判斷且有些 edge case，實作起來較複雜不直觀。以 DP 的角度去解的話，你不需要執著最佳獲利的買入點和賣出點只需要計入買入價格與當前最大獲利。其重點是要確認潛在的最大獲利區間條件，在適當位置更新買入點，過程中需要記錄當下的最大獲利。
    - 此概念類似於 Kadane's Algorithm，主要是要從 array 中找出 maximum subarray sum，透過動態維持`當前最大值`與`全域最大值`兩個變數。`當前最大值`主要是記錄當前 subarray 的狀態，如何決定新的 subarray 開始則是視題目定義。

### Stack
- 20 - Valid Parentheses [[link](https://leetcode.com/problems/valid-parentheses/)]
  - `Easy`、`O(n)`
  - Tags: `String`、`Stack`
  - Note: 此題目在不限制先進後出（First In Last Out，FILO）時，使用 hash table 的方式較直觀，EX. `input: "([)]" Output: True`。而在本題需要確保括號的開與關需要 FILO，則較適合使用 stack 的方式去處理。

### Binary Search 
- 704 - Binary Search [[link](https://leetcode.com/problems/binary-search/)]
  - `Easy`、`O(logn)`
  - Tags: `Array`、`Binary Search`
  - Note: 在已排序的序列的場景下，Binary Search 透過決定左右範圍，每次以中間值判斷要往哪一半的方向搜尋，可以快速查找對應數值。要特別熟悉一下 upper bound 或是 lower bound 版本的實作。
  - <details><summary>Example</summary><b>
 
    #### Exact Value
    ![image](https://github.com/user-attachments/assets/10deeaa8-b375-4ef5-93ea-f076706adb61)
 
    #### Upper bound
    ![image](https://github.com/user-attachments/assets/18124327-fa5d-4563-8873-f4d7e5344c26)
    ![image](https://github.com/user-attachments/assets/2d30b047-433e-4cdd-89c6-33db77173074)

    #### Lower bound
    ![image](https://github.com/user-attachments/assets/9f9aaae5-8ea1-41be-be4d-7f982f5a7da5)


    
    _image frome leetcode -> https://leetcode.com/problems/binary-search/editorial/_

    
    </b></details>
### Linked List
- 21 - Merge Two Sorted Lists [[link](https://leetcode.com/problems/merge-two-sorted-lists)]
  - `Easy`、`O(m+n)`
  - Tags: `Linked List`、`Recursion`
- 141 - Linked List Cycle [[link](https://leetcode.com/problems/linked-list-cycle)]
  - `Easy`、`O(n)`
  - Tags: `Hash Table`、`Linked List`、`Two Pointers`
  - Note: 在 python 中可以直接用 list(dynamic array)、dict(hash table) 去存取已經過節點。Two-Pointers Method (Floyd's Cycle-Finding Algorithm)，，透過兩個遊走速度不一的節點，去判定是否存在循環。要注意的是，它是用在具有明確序列結構的資料，例如鏈結串列、循環數組或迭代函數，並且只能確認循環存在與否，無法得知進一步訊息。
- 206 - Reverse Linked List [[link](https://leetcode.com/problems/reverse-linked-list/)]
  - `Easy`
  - Tags:

### Trees
- 226 - Invert Binary Tree [[link](https://leetcode.com/problems/invert-binary-tree)]
  - `Easy`
  - Tags:
- 104 - Maximum Depth of Binary Tree [[link](https://leetcode.com/problems/maximum-depth-of-binary-tree)]
  - `Easy`
  - Tags:
- 543 - Diameter of Binary Tree [[link](https://leetcode.com/problems/diameter-of-binary-tree)]
  - `Easy`
  - Tags
- 110 - Balanced Binary Tree  [[link](https://leetcode.com/problems/balanced-binary-tree)]
  - `Easy`
  - Tags
- 100 - Same Tree [[link](https://leetcode.com/problems/same-tree)]
  - `Easy`
  - Tags:
- 572 - Subtree of Another Tree [[link](https://leetcode.com/problems/subtree-of-another-tree)]
  - `Easy`
  - Tags:

### Heap / Priority Queue
- 703 - Kth Largest Element in a Stream [[link](https://leetcode.com/problems/kth-largest-element-in-a-stream)]
  - `Easy`
  - Tags:
- 1046 - Last Stone Weight [[link](https://leetcode.com/problems/last-stone-weight)]
  - `Easy`
  - Tags:

### Backtracking

### Tries

### Graphs

### Advanced Graphs

### 1-D DP
- 70 - Climbing Stairs [[link](https://leetcode.com/problems/climbing-stairs)]
  - `Easy`
  - Tags:
- 746 - Min Cost Climbing Stairs [[link](https://leetcode.com/problems/min-cost-climbing-stairs)]
  - `Easy`
  - Tags:

### 2-D DP

### Greedy

### Intervals

### Bit Manipulation
- 136 - Single Number [[link](https://leetcode.com/problems/single-number)]
  - `Easy`、`O(n)`
  - Tags: `Array`、`Bit Manipulation`

### Math & Geometry
- 202 - Happy Number [[link](https://leetcode.com/problems/happy-number)]
  - `Easy`
  - Tags:
- 66 - Plus One [[link](https://leetcode.com/problems/plus-one)]
  - `Easy`
  - Tags:


### Daily
- 1352 - Product of the Last K Numbers  [[link](https://leetcode.com/problems/product-of-the-last-k-numbers/)]
  - `Medium`、`O(nlogm)`
  - Tags: `Array`、`Math`、`Design`、`Data Stream`、`Prefix Sum`
  - Note: 在需要多次查詢區間資料和或是相乘的情況下，透過前綴和(Prefix Sum)或是前綴乘(Prefix product)的小技巧，可以有效提高運行效率。

- ★ 2342 - Max Sum of a Pair With Equal Sum of Digits [[link](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/)]
  - `Medium`、` implement both GetProduct and Add to work in O(1) time complexity`
  - Tags: `Array`、`Hash Table`、`Sorting`、`Heap (Priority Queue)`

- ★ 2375 - Construct Smallest Number From DI String  [[link](https://leetcode.com/problems/construct-smallest-number-from-di-string/)]
  - `Medium`、`O(n)`
  - Tags: `String`、`Backtracking`、`Stack`、`Greedy`、`recursion`
  - Note: 在一些限制下，暴力解也是一種方法。但是可以透過一些技巧，進一步減少暴力解的時間複雜度。這題遞迴和 stack 的方式不直觀需要多看幾次。在題目的條件下，基本上序列只會有嚴格遞增(I) or 遞減(D)，因為如此可以較簡單的角度去處理這個問題。
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

- ★ 2523 - Closest Prime Numbers in Range [[link](https://leetcode.com/problems/closest-prime-numbers-in-range)]
  - `Medium`、`O(right * log(log(right))) using Sieve of Eratosthenes` 
  - Tags: `Math`、`Number Theory`
  - Note: 主要問題是優化判斷質數(prime) 的方法，如果直接搜尋 2~n 的所有數字去判斷是否整除，會超時。主要用兩種方式優化判斷質數的方式:
    1. 依據數學定理我們可以直接限制搜尋範圍到 n 的平方根 (Square root)。
    2. 使用經典的方法質數篩子 (Sieve of Eratosthenes)，可以一次判斷 1 ~ n 範圍內的所有質數。在本題中將 right 視為n，取的n以下所有質數後再去取出 left ~ right 的質數。

- ★ 2529 - Maximum Count of Positive Integer and Negative Integer [[link](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer)]
  - `Easy`、`O(log n)` 
  - Tags: `Array`、`Binary Search`、`Counting`
  - Note: 可以簡單使用兩個變數去計數，在題目中有特別提到 `non-decreasing` 所以可以使用 Binary Search 的方式做。也就是每此從中間切一半，判斷要往哪裡限縮範圍。這題需要再加強順逆向優先的 binary search 的實作方式。

- 2965 - Find Missing and Repeated Values [[link](https://leetcode.com/problems/find-missing-and-repeated-values)]
  - `Medium`、`O(n^2)` 
  - Tags: `Array`、`Hash Table`、`Math`、`Matrix`
    
- 3066 - Minimum Operations to Exceed Threshold Value II  [[link](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii)]
  - `Medium`、`O(nlogm)` 
  - Tags: `Array`、`Heap (Priority Queue)`、`Simulation`

- 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray [[link](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray)]
  - `Easy`、`O(1)`
  - Tags: `Array`



## Reference
- [Neetcode-150-and-Blind-75](https://github.com/envico801/Neetcode-150-and-Blind-75/tree/main)
- [Neetcode150](https://neetcode.io/practice?tab=neetcode150)
