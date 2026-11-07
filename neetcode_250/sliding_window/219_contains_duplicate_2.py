class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                # remove the item from the window
                window.remove(nums[L])
                # and shift the window
                L += 1
            if nums[R] in window:
                return True
            # if not present and within window size, then we can add
            window.add(nums[R])
        return False
