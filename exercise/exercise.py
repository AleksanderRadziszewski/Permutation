def biggerIsGreater(word):
    arr = list(word)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return " no answer"

    # Finding rightmost succesor to pivot in suffix

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse the suffix

    arr[i:] = arr[len(word) - 1: i - 1: -1]
    print("".join(arr))


biggerIsGreater("dkhc")