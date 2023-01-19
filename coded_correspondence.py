import string
#import enchant

alphabet = string.ascii_lowercase
#d = enchant.Dict("en_US")

v_msg = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
my_msg = "Oh hey! How is it going? Thanks for the puzzle, it was a lot of fun!"
v_msg2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
v_msg3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
offset = 10

def decode_msg(msg, offset):
    decoded_msg = ''
    for letter in msg:
        if letter in alphabet:
            if (alphabet.index(letter) + offset) >= len(alphabet):
                decoded_msg += alphabet[((alphabet.index(letter) + offset) % len(alphabet))]  
            else:  decoded_msg += alphabet[(alphabet.index(letter) + offset)]
        else: decoded_msg += letter
    return decoded_msg
  
def encode_msg(msg, offset):
    decoded_msg = ''
    for letter in msg:
        if letter in alphabet:
            decoded_msg += alphabet[(alphabet.index(letter) - offset)]
        else: decoded_msg += letter
    return decoded_msg

def decode_msg_vig(msg, code):
    x = 0
    decoded_msg = ''
    for letter in msg:
        if letter in alphabet:  
            decoded_msg += alphabet[(alphabet.index(letter) - alphabet.index(code[x % len(code)]))]
            x += 1
        else: decoded_msg += letter
    return decoded_msg

def encode_msg_vig(msg, code):
    x = 0
    encoded_msg = ''
    for letter in msg:
        if letter in alphabet:
            if (alphabet.index(letter) + alphabet.index(code[x % len(code)])) >= len(alphabet):
                encoded_msg += alphabet[((alphabet.index(letter) + alphabet.index(code[x % len(code)])) % len(alphabet))]  
            else: encoded_msg += alphabet[(alphabet.index(letter) + alphabet.index(code[x % len(code)]))]
            x += 1
        else: encoded_msg += letter
    return encoded_msg

print(decode_msg(v_msg, offset))  

print(encode_msg(my_msg, offset))

print(decode_msg(v_msg2, offset))
print(decode_msg(v_msg3, (offset + 4)))

hard_msg = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

def brute_decode_msg(msg):
    for i in range(25):
        print(decode_msg(msg, i))
    return True

### junyper notebook didn't have PyEnchant and goal was to repeat 25 times as output
#      decoded = decode_msg(msg, i)
#        decoded.split()
#        if d.check(decoded[1]) == True:
#            return decoded
      
#print(brute_decode_msg(hard_msg))
brute_decode_msg(hard_msg)
            
vig_msg = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
code_word = "friends"
print(decode_msg_vig(vig_msg,code_word))
              
my_msg = "I'm so happy to have done this exercise! I feel like you have taught me a lot!"
code_word = "success"

print(encode_msg_vig(my_msg, code_word))
vig_coded_msg = encode_msg_vig(my_msg, code_word)

print(decode_msg_vig(vig_coded_msg, code_word))
