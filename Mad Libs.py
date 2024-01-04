def get_input(word_type):
    user_input : str = input(f"Enter a {word_type}:")
    return user_input


noun1 = get_input("noun")
verb = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = (f"Once upon a time, in a bustling city, "
         f"there was a lively bakery run by a cheetah"
         f" named Carl. Every day, Carl would {verb} "
         f"around the kitchen, whisking ingredients together"
         f" with lightning speed. One day, a mischievous {noun1} "
         f"named Sparkles entered the {noun2} and {verb2} the flour all over "
         f"the place, creating a cloud that covered the entire room. "
         f"Carl, with a mixture of surprise and laughter, chased Sparkles around the bakery, "
         f"finally catching the playful troublemaker and turning the flour fight into a "
         f"baking adventure they'd both remember forever.")

print(story)

