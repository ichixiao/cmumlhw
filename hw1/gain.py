'''
code published in http://www.onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html
for learning python and clear the thoughts
'''
def gain(data, attr, target_attr):

    val_freq = {}
    subset_entropy = 0.0

    for record in data:
        if (val_freq.has_key(record[attr])):
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    for val in val_freq.keys():
        val_prob = val_freq[val]/sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]
        subset_entropy += val_prob * entropy(data_subset, target_attr)

    #subtract the entropy of the chosen attribute from the entropy of the whole data set with respect to the target attribute
    return (entropy(data, target_attr) - subset_entropy)