from hamming import Hamming
import platform
import os


def main():
    clean_screen()
    
    while True:
        show_message('Hamming algorithm', 20)
        word = input('type the bits: ')
        parity = input('type parity "even" or "odd": ')
        communication_type = input('send or receive? ')

        if communication_type == 'send':
            if not send(word, parity):
                show_message('Invalid data', 20)

        elif communication_type == 'receive':
            if not receive(word, parity):
                show_message('Invalid data', 20)

        else:
            show_message('Invalid data', 20)

        again = input(' >>> press "0" and then "Enter" to STOP <<< ')
        clean_screen()
        if again == '0':
            break


def show_message(word, line_number):
    print()
    print('='*line_number)
    print(word)
    print('='*line_number)
    print()


def clean_screen():
    try:
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
    except Exception:
        pass


def send(word, parity):
    hamming = Hamming(word, parity)
    if hamming.word_generate():
        print()
        print('='*50)
        print('Typed word: ', end='')
        print(word)
        print('generated word: ', end='')
        print(hamming.word_distributed)
        print('='*50)
        print()
        return True
    return False


def receive(word, parity):
    hamming = Hamming(word, parity)
    if hamming.check_word():
        print()
        print('='*50)
        print(hamming.word_distributed)
        if hamming.error_counter > 0:
            print('incorrect word')
            print('error found in position {}'.format(hamming.error_position))
        else:
            print('correct word')
        print('='*50)
        print()
        return True
    return False


if __name__ == '__main__':
    main()
