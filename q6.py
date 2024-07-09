#I am using a dictionary method to store the numbers, then using loops for specific use cases.

def number_to_words(n):
    words = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
             10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
             60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}
    
    if n == 0:
        return 'zero'

    def to_words(n):
        if n < 20:
            return words[n]
        elif n < 100:
            return words[n // 10 * 10] + (words[n % 10] if n % 10 != 0 else '')
        elif n < 1000:
            return words[n // 100] + 'hundred' + ('and' + to_words(n % 100) if n % 100 != 0 else '')
        else:
            return to_words(n // 1000) + 'thousand' + to_words(n % 1000)

    return to_words(n)

def count_letters(number):
    words = number_to_words(number)
    #To remove spaces and hyphens
    words = words.replace(' ', '').replace('-', '')
    return len(words)

#number = 1000
number = int(input("Enter a number between 1 to 1001:"))
print(f"The number of letters in '{number}' is: {count_letters(number)}")
