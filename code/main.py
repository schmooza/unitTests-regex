from __init__ import *
import pandas as pd

userData = pd.read_csv("data/myData.csv")

print (userData)
# init
pass_test = Tracking_results()
pass_test.set_val(0)
check = pass_test.get_val()


# test
#instantiate the get methods class.
g = Get_list_of_methods_in_class()

# get a list of methods from the test class
methodListDirivedFromClass = g.method_one()

#instantiate the test class
testTheData = Test_if_legal_string()

if check == 0:
#iterates through all the tests (methods).
	for method_test in methodListDirivedFromClass:

	# extracts the name from the list
		method_to_call = getattr(testTheData,method_test)

	# feeds the dataset to the tests


		for item in userData.iloc[0]:

			if check == 0:

				result = method_to_call(item)
				# print(result,"debug return val")
				pass_test.set_val(result)
				pass_test.get_val()
				# print ('next')
				check = pass_test.get_val()

			elif check == 1:
				pass
#
#
#
#
# a = Students()
#
#
#
# # test
#
#
# t.test_string_input1(a.method_one([2,2.4,True]))
# t.test_string_input2(a.method_one(""))
# t.test_string_input3(a.method_one("  a "))
# t.test_string_input4(a.method_one("12345678910"))
# t.test_string_input5(a.method_one("\\"))
#
# print("\n")
# t.test_string_input1(a.method_one(["a"]))
# t.test_string_input2(a.method_one("aa"))
# t.test_string_input3(a.method_one("a"))
# t.test_string_input4(a.method_one("1234567890"))
# t.test_string_input5(a.method_one("aaaa"))