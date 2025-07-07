returns -1 when not found:

pos = haystack.find(needle)
pos = haystack.find(needle, offset)
raises ValueError when not found:

pos = haystack.index(needle)
pos = haystack.index(needle, offset)
To simply test if a substring is in a string, use:

needle in haystack
which is equivalent to the following PHP:

strpos(haystack, needle) !== FALSE