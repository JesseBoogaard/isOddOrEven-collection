# Elixir, N processes

For a given number `N`, this will spawn `N` Erlang processes. Each process
will send a message back to the parent, and the parent will flip the odd/even
result on each received message. When no messages arrive after one second,
the function in the parent thread will return the result.

## Usage

You'll need [Elixir](https://elixir-lang.org)
[installed](https://elixir-lang.org/install.html).

```bash
$ iex is_odd_or_even.ex
```
```elixir
iex(1)> IsEvenOrOdd.check(3)
:odd
iex(2)> IsEvenOrOdd.check(1_000_000)
:even
```
