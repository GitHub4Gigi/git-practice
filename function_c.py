def merge_lists(list_a, list_b):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    # turn lists into sets
    set_a = set(list_a)
    set_b = set(list_b)
    # make union set which will combine sets without duplicates
    union_set = set_a.union(set_b)
    # turn union set back into list
    new_list = list(union_set)

    return new_list


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
