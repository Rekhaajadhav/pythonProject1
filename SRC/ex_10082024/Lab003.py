# commands in Python

# Builtsin.py - module provides direct access to all 'built-in' identifiers of Python like utilities
'''def print(*values: object,
          sep: str | None = " ",
          end: str | None = "\n",
          file: SupportsWrite[str] | None = None,
          flush: Literal[False] = False) -> None
Prints the values to a stream, or to sys. stdout by default.

sep
string inserted between values, default a space.
end
string appended after the last value, default a newline.
file
a file-like object (stream); defaults to the current sys. stdout.
flush
whether to forcibly flush the stream.
`print(*values, sep=" ", end="\n", file=None, flush=False)` '''

print("It", "is", "used", "to", "print", "the", "values", "to", "a", "stream")

print("It","is","used","to","print","the","values","to","a","stream","with","seperator",sep=" | ")

print("It", "is", "used", "to", "print", "the", "values", "to", "a", "stream"," with","end", end=".")
