class Trie():
    def __init__(self):
        self.root = {}

    def check_and_update(self, word):
        is_new_word = False
        current = self.root #explain why!

        for char in word:
            if char not in current:
                is_new_word = True
                current[char] = {}
            current = current[char]

        #invariant: traverse all char in word. We have NOT seen end marker,
        # i.e. only seen prefix up to this point
        if 'End' not in current:
            is_new_word = True #Prefix of larger word is now a new word
            current['END'] = {}

        return is_new_word