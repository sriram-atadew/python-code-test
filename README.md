# Problem Statement
> We need a way of finding all the occurrences of a particular
set of characters in a string. It should
- Accept two strings as input. One called 'textToSearch'
and one called 'subtext'
- The solution should match the subtext against the
textToSearch, outputting the positions of the beginning
of each match for the subtext within the textToSearch.
- Multiple matches are possible
- Matching is case insensitive
- If no matches have been found, no output is generated

>Sample Acceptance Criteria
Text:

textToSearch = "Peter told me that peter the pickle piper
piped a pitted pickle before he petered out. Phew!"

> Subtext: Expected Result

Peter "1, 20, 75"

peter "1, 20, 75"

pick "30, 58"

pi "30, 37, 43, 51, 58"

z "\<No Output\>"

Peterz "<\No Output\>"

# To run this code
`python main.py`

# To run test cases
`python -m unittest tests.test_subtext_position`
