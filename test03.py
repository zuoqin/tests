import sys

sys.path.append("/usr/local/lib/python2.7/site-packages/")


import oerplib
def read_unicode(text, charset='utf-8'):
    if isinstance(text, basestring):
        if not isinstance(text, unicode):
            text = unicode(obj, charset)
    return text

# Prepare the connection to the server
oerp = oerplib.OERP('localhost', protocol='xmlrpc', port=8069)

# Check available databases
print(oerp.db.list())

# Login (the object returned is a browsable record)
user = oerp.login('admin', 'Qwerty123', 'podushka')
print(user.name)            # name of the user connected
print(user.company_id.name) # the name of its company

# Simple 'raw' query
user_data = oerp.execute('res.users', 'read', [user.id])
print(user_data)

# Use all methods of a model class
order_obj = oerp.get('sale.order')
order_ids = order_obj.search([])

str1 = ""
for order in order_obj.browse(order_ids):
    i = 0
    print(order.name)
    products={}
    for line in order.order_line:
        if len(line.product_id.name.encode('utf-8')):



            products = line.product_id.name
            #products[i] = bytes(line.product_id.name.encode('utf-8'))

            i+=1
            str1 = str( i )
            print(str1)
            print bytes(products.encode('utf-8'))
    #print products

    #products = [line.product_id.name.encode('utf-8') for line in order.order_line]
    #print bytes(products)
    
    #str2 = str1.decode('unicode-escape')
    #print str2.encode('utf-8')    
    #print(products)
    #print(str1)