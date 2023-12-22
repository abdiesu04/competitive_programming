class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        for idx , word in enumerate(words):
            if word[0] == '$':
                try:
                    price = int(word[1:])
                except ValueError:
                    continue
                price -= price * discount / 100
                words[idx] = f'${price:.2f}'
        return ' '.join(words)
