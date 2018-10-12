import kronos
import random
 
@kronos.register('0 */2 * * *')
def talk():
    print "it works"