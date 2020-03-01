# RiverCrossingPuzzles
A project to implement a wide variety of river crossing puzzles into one application

## Organization

The project itself is in `riverCrossing`. The tests are in module `tests`, with some old code in
`oldsrc`.

`images` holds images for the gui, and `rules` holdes game rules definitions.

Run the tests with:

```bash
python3 -m unittest discover riverCrossing
```

### On Organization and Imports

Python has a concept of "modules" which organize code. Within a module, the module
itself is called "." and the files within the module can be referred to as ".filename",
omitting the .py.

Our module, `riverCrossing`, has both a `__init__.py` file, which is what makes it a
module, and a `__main__.py` file, which makes it an executable.

This means you can run it with:

`python3 -m riverCrossing` followed by either `console` for the console or `gui` for the
gui game. This should also fix issues for those using IDEs.

## Dependencies
Dependencies are in `requirements.txt`. Install them with `pip3 -r requirements.txt`
