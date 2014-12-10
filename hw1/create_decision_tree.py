'''
code published in http://www.onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html
for learning python and clear the thoughts
'''
def create_decision_tree(data, attributes, target_attr, fitness_func):
    data = data[:]
    #
    vals = [record[target_attr] for record in data]

    if not data or (len(attributes) - 1) <= 0:
        return default
    # all the records have the same classification
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        #choose the next best attribute to best classify data
        best = choose_attribute(data, attributes, target_attr, fitness_func)

        #create a new decision tree/node with the best attribute and an empty dictionary objecy
        #
        tree = {best:{}}

        #create a new decision tree/sub-node for each of the values in the best attribute field
        for val in get_values(data, best):
            #create a subtree for the current value under the "best" field
            subtree - create_decision_tree(get_examples(data, best, val),
                                           [attr for attr in attributes if attr != best],
                                           target_attr,
                                           fitness_func)
            #add thenew subtree to the empty dictionary object in our new tree/node we just created
            #
            tree[best][val] = subtree

    return tree