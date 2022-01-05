input = elem(File.read("data.txt"), 1)
vals = String.graphemes(input)
lefts = Enum.count(vals, fn x -> x == "(" end)
rights = Enum.count(vals, fn x -> x == ")" end)

IO.puts(lefts - rights)
