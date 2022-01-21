# wordle-solver
Solve wordle puzzles.

Run `$ python wordle.py`.

Program will ask for a guess and the score and will then generate a list of
potential next guesses.

## Example Usage
Suppose the word to be guessed is "table". Then a potential series of guesses
might look like this:
```
Initial guess suggestion: irate
7373 possible options
Tried guess: irate
Grade for guess: bbbby
620 possible next guesses
random possible next guesses:
['kenny', 'foley', 'coley', 'nodes', 'klees', 'memes', 'menus', 'desks', 'godel', 'defog']
Tried guess: nodes
Grade for guess: bgggb
7 possible next guesses
['modem', 'godel', 'model', 'codex', 'yodel', 'boded', 'coded']
Tried guess: model
Grade for guess: ggggg
Found solution: model
```
