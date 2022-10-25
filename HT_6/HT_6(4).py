'''
4. Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить декодоване значення (латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensitive (на ваш розсуд - великими чи маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть. Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..-- -...   .. ...   .... . .-. .
    результат: GEEKHUB IS HERE
'''

english_morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '' : ''}

morse_english_dict = {}

def morse_code(code_entry):

    
    for key, value in english_morse_dict.items():
        morse_english_dict[value] = key

    english = []
    code_entry = code_entry.split(' ')
    for code in code_entry:
        if code in morse_english_dict:
            english.append(morse_english_dict[code])
            eng = ' '.join(english)
            
    print(f'Translation morse to english:\n{eng}')

    morse = []
    message = input('Enter message: ')
    message = message.upper()
    for char in message:
        if char in english_morse_dict:
            morse.append(english_morse_dict[char])
    morse = ''.join(morse)
    print(f'Translation english to morse:\n{morse}')
          
  


code_entry = input('Enter morse code: \n')


morse_code(code_entry)
