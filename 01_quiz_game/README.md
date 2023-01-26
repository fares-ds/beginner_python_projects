# Quiz Game with Python

In this python project we build a simple quiz application for terminal.

In this project, you will learn how to:

- Interact with user in the terminal
- How to use python dictionary objects

## Project Description

We have a python dictionary of `10` scientist as keys and there inventions as values:

```python
question_dict = {
    'Ballpoint pen': 'Biro Brothers', 'Jet Engine': 'Sir Frank Whittle',
    'Gramophone': 'Thomas Alva Edison', 'Internal Combustion Engine': 'Otto',
    'The Spinning Jeny': 'James Hargreaves', 'the small pox vaccine': 'Edward Jenner',
    'Railway air brakes': 'George Westinghouse', 'Electric streetcar': 'Thomas Davenport',
    'Electric Generator': 'Michal Faraday', 'Gun Powder': 'Roger Bacon'
    }
```

You need to iterate through the dict keys (inventions) and give the user 4 choices (scientist name), be sure that the choices are random and includes the right answer. The output should look like this:

```console
Q_1 - How invent Electric streetcar
    1 - Roger Bacon
    2 - Sir Frank Whittle
    3 - George Westinghouse
    4 - Thomas Davenport
Enter your choice : 
```


