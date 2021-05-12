import argparse
import random

parser = argparse.ArgumentParser(description='Generate rule-based attack pattern')
parser.add_argument('word', help='word from what the pattern will be generated')
parser.add_argument('-l', dest='lines', type=int, default=50, help='number of patterns (lines) generated')
parser.add_argument('-o', dest='output_file', help='output file')
args = parser.parse_args()

word = args.word
lines_number = args.lines
output_file = args.output_file

functions = ': l u c C t T{x} r d p{x} f { } ${x} ^{x} [ ] D{x} x{x}{y} O{x}{y} i{x}{y} o{x}{y} \'{x} s{x}{y} @{x} z{x} Z{x} q'
x_arg_pattern = '{x}'
y_arg_pattern = '{y}'
result = ''

def display_result(result):
    print(result)

def generate_output_file(result):
    file = open(output_file, 'w')
    file.write(result)

def generate_duplicate_rule():
    return 'p' + str(random.randint(1, 4))

def generate_random_word_position():
    return random.randint(0, len(word) - 1)

def handle_multiple_args(function):
    return ''

def handle_single_arg(function):
    rule = '';
    letter = function[0]

    if letter == 'p':
        rule = generate_duplicate_rule()
    else:
        rule = letter + str(generate_random_word_position())

    return rule

def generate_patterns(functions):
    splitted_functions = functions.split(' ')
    patterns = ''

    for i in range(lines_number):
        pattern = ''
        pattern_size = random.randint(1, 10)

        for j in range(pattern_size):
            random_function_index = random.randint(0, len(splitted_functions) - 1)
            random_function = splitted_functions[random_function_index]
            pattern_item = ''

            if x_arg_pattern + y_arg_pattern in random_function:
                pattern_item = handle_multiple_args(random_function) 
            elif x_arg_pattern in random_function:
                pattern_item = handle_single_arg(random_function)
            else:
                pattern_item = random_function

            if pattern_item != '':
                pattern += pattern_item

                if j != pattern_size:
                    pattern += ' '

        if pattern != '':
            patterns += pattern

            if i != lines_number:
                patterns += '\n'

    return patterns

def main():
    result = generate_patterns(functions)   
    display_result(result)

if __name__ == '__main__':
    main()


if output_file:
    generate_output_file(result) 
