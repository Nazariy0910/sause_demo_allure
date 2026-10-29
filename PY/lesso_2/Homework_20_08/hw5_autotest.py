expected_title = 'Home page'
expected_button = 'Join'
expected_price = 1500
a= input('Enter title ')
b= input('Enter button ')
c= int(input('Enter price '))
if expected_title == a:
    print('✅ PASSED')
else:
    print('❌ FAILED')

if expected_button == b:
    print('✅ PASSED')
else:
    print('❌ FAILED')

if expected_price == c:
    print('✅ PASSED')
else:
    print('❌ FAILED')    