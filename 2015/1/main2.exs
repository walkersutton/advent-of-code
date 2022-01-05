input = elem(File.read("data.txt"), 1)
vals = String.graphemes(input)

defmodule Scratch do
	def initial_basement_index([head | tail], floor) do
		cond do
			floor == -1 ->
				0
			head == ")" ->
				1 + initial_basement_index(tail, floor - 1)
			head == "(" ->
				1 + initial_basement_index(tail, floor + 1)
		end
	end
end

IO.puts(Scratch.initial_basement_index(vals, 0))
