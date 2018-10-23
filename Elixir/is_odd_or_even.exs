# Copyright (c) 2018 Michał Szewczak
#
# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to
# deal in the Software without restriction, including
# without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom
# the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

defmodule IsEvenOrOdd do
  @doc """
  Checks if the given number N is even or odd by spawning N processes which
  send a message back and flipping the result on each received message.
  """
  def check(number) do
    # Get own process ID.
    parent = self()

    # Define a sender which will send a message back to the parent.
    sender = fn ->
      send(parent, :message)
    end

    # Spawn N workers.
    1..number
    |> Enum.each(fn _ ->
      spawn(sender)
    end)

    # Wait for messages and flips the passed in boolean after each one. When no
    # message is received after one second, return the result.
    if count(true), do: :even, else: :odd
  end

  defp count(is_even) do
    receive do
      :message -> count(!is_even)
    after
      1_000 -> is_even
    end
  end
end
