#This program is directly taking from professor's. All credits to him.
#This is the program that generates a message and converts it into a hex string.

#Two imports, codecs and random. Codecs is needed for the conversion, and random is needed to get the amount of NULL messages before and after the message.
import codecs
import random

STX = "02"
ETX = "03"
SOH = "01"
EOT = "04"
NULL = "00"

class Serialization():
    
    #Function get_userascii that converts a string to hexadecimal.
    def get_userascii(self, user_input):
        format_string =""
        for element in user_input:
            hex(ord(element))
            character_string = format(ord(element), "x")
            format_string = format_string + character_string
        return format_string

    def make_message(slef, transmitted_string):
        frontnum_NULL = random.randint(1,6)
        backnum_NULL = random.randint(1,6)
        final_string = (frontnum_NULL * NULL) + transmitted_string + (backnum_NULL * NULL)
        return final_string
    
    def serialize(self, input_str):
        print(input_str)
        format_string = self.get_userascii(input_str)
        print(format_string)
        framed_string = STX + format_string + ETX
        print("this is framed_string: ",framed_string)
        transmitted_string = 3*SOH + STX + format_string + ETX
        + 3*EOT
        print("this is transimtted_string: ", transmitted_string)
        message_string = self.make_message(transmitted_string)
        print("this is final_messge", message_string)
        return message_string
