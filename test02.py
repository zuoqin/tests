# def outer(some_func):
#         def inner():
#             print "before some_func"
#             ret = some_func() # 1
#             return ret + 1
#         return inner
# def foo():
#         return 1
# decorated = outer(foo)
# print(decorated())



str1 = '' \
    'select sum(product_qty), product_id, product_uom '\
    'from stock_move '\
    'where location_id NOT IN %s '\
    'and location_dest_id IN %s '\
    'and product_id IN %s '\
    'and state IN %s '


where = [(12,), (12,),
    (3, 23, 5, 4, 2, 6, 7, 8, 12, 10, 11, 9, 16, 21, 22, 24, 20, 13, 25, 27, 28, 29, 30, 31, 14, 26, 1),
    ('confirmed', 'waiting', 'assigned', 'done')]


print str1 % tuple(where)

#print str2