n = len(nums)
        arr = [0] * n  # Create a list with the same size and initialize with 0
        j = 0

        for i in range(n):
            if nums[i] != 0:
                arr[j] = nums[i]
                j += 1

        # Copy the result back to the original list
        for i in range(n):
            nums[i] = arr[i]
