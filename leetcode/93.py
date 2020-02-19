class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        # NOTE : check leading zero!!!
        def check(digits):
            # NOTE : allow zero itself
            if digits == '0': return True
            if digits[0] == '0':
                return False
            return int(digits) <= 255
        
        # if N block lefts, N <= the number of digits <= 3N
        def restore(block_left, cur_address, remain_digits):
            if not(block_left <= len(remain_digits) <= block_left * 3):
                return
            
            if block_left == 1:
                if check(remain_digits):
                    cur_address += remain_digits
                    result.append(cur_address)
            else:
                # Assign digits for current block
                for i in range(1, 4):
                    if check(remain_digits[:i]):
                        restore(block_left-1, cur_address+remain_digits[:i]+'.', remain_digits[i:])
        restore(4, '', s)
        return result
                
