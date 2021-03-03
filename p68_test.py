from p68 import Solution

test_cases = [
    (
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
    ),
    (
        (["What","must","be","acknowledgment","shall","be"], 16),
        [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
    ),
    (
        (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ],
    )
]


def test_fullJustify():
    s = Solution()
    for case in test_cases:
        assert s.fullJustify(*case[0]) == case[1], case
