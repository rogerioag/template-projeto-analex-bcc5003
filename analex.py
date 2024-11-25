# from automata.fa.Moore import Moore
import sys, os

from myerror import MyError

error_handler = MyError('LexerErrors')

global check_cm
global check_key

# moore = Moore(['q0', 'q1', 'q2', 'q3', 'q4'],
#               ['i' , 'n' , 't', ' '],
#               ['INT', 'ELSE'],
#               {
#                   'q0' : {
#                       'i' : 'q1',
#                   },
#                   'q1': {
#                       'n': 'q2',
#                   },
#                   'q2': {
#                       't': 'q3',

#                   },
#                   'q3': {
#                       '\n': 'q4',
#                   }
#               },

#               'q0',
#               {
#                   'q0' : '',
#                   'q1' : '',
#                   'q2' : '',
#                   'q3' : '',
#                   'q4' : 'INT'
#               }
#               )

def main():
    check_cm = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        # print("Argument #{} is {}".format(idx, arg))
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if(arg == "-k"):
            check_key = True
    
    # print ("No. of arguments passed is ", len(sys.argv))

    if(len(sys.argv) < 3):
        raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

    if not check_cm:
      raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        data = open(sys.argv[idx_cm])
        source_file = data.read()

        if not check_cm:
            print("Definição da Máquina")
            print(moore)
            print("Entrada:")
            print(source_file)
            print("Lista de Tokens:")
        
        #print(moore.get_output_from_string(source_file))


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError):
        print(e)