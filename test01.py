import sys

sys.path.append("/usr/local/lib/python2.7/site-packages/")


import magento

url = 'http://127.0.0.1/magento'
url = 'http://lifemallerp.preprodbysoftchina.com'
apiuser = 'zuoqin'
apipass = 'Qwerty123'



#with magento.Product(url, apiuser, apipass) as product_api:
#    order_filter = {'created_at':{'from':'2011-09-15 00:00:00'}}
#    products = product_api.list(order_filter)

#for Product in products:
#    print(Product)


with magento.API(url, apiuser, apipass) as magento_api:
    # Calling custom APIs if you have extension modules on your
    # magento installation
    #res = magento_api.call('product_stock.update', [ 'SKU01',{'qty': '111','is_in_stock': '1', 'manage_stock': '1'}])
    #res = magento_api.call('product_stock.update', [ 8 ,{'qty': '333','is_in_stock': '1', 'manage_stock': '1'},False,'id'])
    
    #print(res)
    #res = magento_api.call('ol_catalog_product.update', [8, {'color': '5'}, False, 'id'])
    #print(res)
    #res = magento_api.call('ol_catalog_product.update', [8, {'additional_attributes': { 'multi_data' : {'key':'color','value':4}}}, False, 'id'])
    #print(res)
    #res = magento_api.call('catalog_product.update', ['8', { 'weight': '1111'}, False, 'id'])
    #res = magento_api.call('catalog_product.update', [8, {'additional_attributes': {'singledata' : {   'key':'color','value':'4'  }}}, False, 'id'])
    #res = magento_api.call('ol_catalog_product.info', ['10'])
    #print(res)
    #store_group = magento_api.call('ol_groups.list', [])
    #store_views = magento_api.call('ol_storeviews.list', [])
    res = magento_api.call('sales_order.addComment', ['300000346', 'Canceled'])
    #print(res)
    #res = magento_api.call('catalog_product.create', ['simple', '4', 'SKU99991', {'status': '1', 'description': 'description', 'weight': '111', 'websites': 1, 'price': '1115', 'visibility': '4', 'tax_class_id': '4', 'short_description': 'short_description', 'categories': 2, 'name': 'product name'}])

    #res = magento_api.call('ol_catalog_product.update', [247, {'visibility': '4', 'manage_stock': 1}, False, 'id'])
    #res = magento_api.call('catalog_product_attribute_set.list',[])
    #res = magento_api.call('catalog_product_attribute.list', [])
    #res = magento_api.call('product_attribute.create',[{'attribute_code': 'yaschik2','scope':'global',
    #    'default_value':'tonliy', 'apply_to':['simple','configurable'],
    #    'frontend_input':'select', 'is_unique':0, 'is_required':0, 'is_configurable':1,'is_searchable':0,
    #    'frontend_label':[{'store_id':'0', 'label': 'yaschik1'},{'store_id':'1', 'label': 'yaschik2'},{'store_id':'2', 'label': 'yaschik3'}]}] )
    
    # res = magento_api.call('product_attribute.addOption',[137,
    #     {'label':[
    #     {'store_id':'0', 'value': 'white'},
    #     {'store_id':'1', 'value': 'white'},
    #     {'store_id':'2', 'value': 'white'}],
    #     'order':1,'is_default':'1'}])
    # res = magento_api.call('product_attribute.addOption',[137,
    #     {'label':[
    #     {'store_id':'0', 'value': 'blue'},
    #     {'store_id':'1', 'value': 'blue'},
    #     {'store_id':'2', 'value': 'blue'}],
    #     'order':0,'is_default':'0'},

    #     ] )
    #res = magento_api.call('product_attribute.update',[137,[{'default_value':}]
    #res = magento_api.call('product_attribute_set.attributeAdd',[269, 11])
    #res = magento_api.call('catalog_product.update', [18, {'websites': [0,1]}])
    print(res)


#INVENTORY_FIELDS = ('manage_stock',
#                    'tax_class_id',
#                    'backorders',
#                    'magento_qty',
#                    )
#vals = {'manage_stock': 'yes'}
#val2 = {'tax_class_id': '2'}
#print (set(val2).intersection(INVENTORY_FIELDS))

