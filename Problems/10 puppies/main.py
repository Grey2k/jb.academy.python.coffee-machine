class Puppy:
    n_puppies = 0  # number of created puppies

    # define __new__
    def __new__(cls):
        if Puppy.n_puppies < 10:
            Puppy.n_puppies += 1
            return object.__new__(cls)

        return None
