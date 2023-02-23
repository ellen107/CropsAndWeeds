import splitfolders


#split into training, testing, and validation
splitfolders.ratio("weeds2", output="output",
    seed=1337, ratio=(.8, .1, .1), group_prefix=None, move=False) # default values
