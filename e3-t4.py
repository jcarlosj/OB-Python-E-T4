# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso

limite = 100

# Forma 1
# for i in reversed( range( limite + 1 ) ) :
#     if( i != 0 ) :
#         print( i )

# Forma 2
for i in range( 100, 0, -1 ) :
    print( i )