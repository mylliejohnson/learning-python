# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(out, word):
  print(out[0:2:] + word + out[2::]) 

#make_out_word('[[]]', 'helloo')


# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(str):
    half = int(len(str)/2)
    #print(half)
    print(str[0:half])

#first_half("MYLLIE") 


# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):
  print(a[1:len(a)] + b[1:len(b)] )

#non_start("myllie", 'hello')


# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
   print((str[-2] + str[-1])*3)

#extra_end("hello")

def without_end(str):
    print(str[1:len(str) -1])

#without_end("myleika")

def left2(str):
    print(str[2:] + str[0:2])

#left2("myleika")

def make_tags(tag, word):
  open = "<" + tag + ">"
  close = "</" + tag + ">"
  print(open + word + close)

make_tags("python", "lang")


def string_splosion(str):
    final = ""
    for i in range(len(str)):
        final = final + str[:i+1] + "\n"
    return final

string_splosion("myllie")


def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4

    for x in range(0,4):
       if nums[x] == 9:
           print(True)

# array_front9([1, 2, 9, 3, 4]) 

def last2(str):
    if len(str) < 2:
        return 0

    lastchars = str[len(str)-2:]
    count = 0

    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == lastchars:
            count += 1

    print(count)

last2('axhhax')