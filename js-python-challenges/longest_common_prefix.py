"""Write a function to find the longest common prefix string amongst an array of strings."""


def longest_common_prefix(strings: list[str]) -> str:
    if not strings:
        return ""

    prefix = strings[0]
    for string in strings:
        while string.find(prefix, 0) != 0:
            prefix = prefix[:-1]
            if len(string) < 1:
                return ""
    return prefix


if __name__ == "__main__":
    strings = ["flower", "flow", "flight"]
    result = longest_common_prefix(strings)
    print(result)
