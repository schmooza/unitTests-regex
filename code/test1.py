import re
import inspect
import types

class Get_list_of_methods_in_class():

	def method_one(self):


		# gets all the methods in the test class and returns a list of them to main
		a = Test_if_legal_string()
		methodList = [n for n, v in inspect.getmembers(a, inspect.ismethod)
              if isinstance(v,types.MethodType)]
		return methodList


class Tracking_results():

	def __init__(self, ):
		self.__testReturnVal = None

	def set_val(self,testReturnVal):
		self.__testReturnVal = testReturnVal

	def get_val(self):
		# print(self.__testReturnVal, "debug - value stored in private variable")
		return self.__testReturnVal




class Test_if_legal_string():
	CLASS_CONSTANT_PASS = 0
	CLASS_CONSTANT_FAIL = 1

	def test_string_input1(self,valueIs):
		# note in this case valueIs is a list.

			if valueIs == str(valueIs):
				print(f"pass test, {valueIs} is a string")
				return Test_if_legal_string.CLASS_CONSTANT_PASS
			elif valueIs != str(valueIs):

				print(f"{valueIs} is not a string.")
				return Test_if_legal_string.CLASS_CONSTANT_FAIL

			else:
				print("error in method 1")




	def test_string_input2(self,valueIs):


		if not valueIs:
			print(f"fail test, {valueIs} an empty string")
			return Test_if_legal_string.CLASS_CONSTANT_FAIL

		else:
			print("pass test, some data there")
			return Test_if_legal_string.CLASS_CONSTANT_PASS


	def test_string_input3(self, valueIs):
		valueIs = str(valueIs)
		re1 = bool(re.search(r"\s", valueIs))

		if re1 == True:

			print (f"error {valueIs}, has spaces in the data>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			return Test_if_legal_string.CLASS_CONSTANT_FAIL


		elif re1 == False:
			print(f"pass, {valueIs} has no spaces in the data")
			return Test_if_legal_string.CLASS_CONSTANT_PASS

		else:pass


	def test_string_input4(self, valueIs):

		if len(valueIs) <= 10:
			print ("pass, 10 or less characters")
			return Test_if_legal_string.CLASS_CONSTANT_PASS

		else:
			print("fail, too many letters>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			return Test_if_legal_string.CLASS_CONSTANT_FAIL

	def test_string_input5(self, valueIs):
		# creates an object of all the illegal characters
		pattern = re.compile(r'[@_!#$%^&*()<>?/\\|}{~:]')

		# finds all illegal characters
		illegal_chars =  pattern.findall(valueIs)

		# checks the length of illegal characters to see if it contains data, zero data is good.
		if len(illegal_chars)==0:
			print(f"Pass, {illegal_chars}")
			return Test_if_legal_string.CLASS_CONSTANT_PASS
		else:
			print(f"Fail {illegal_chars}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			return Test_if_legal_string.CLASS_CONSTANT_FAIL


# prog = re.compile(pattern)
# result = prog.match(string)


# def clean_topic_message(self):
#     topic_message = self.cleaned_data['topic_message']
#     invalid_chars = '^<>/\{}[]~`$'
#     if (topic_message == ""):
#         raise forms.ValidationError(_(u'Please provide a message for your topic'))
#     if set(invalid_chars).intersection(topic_message):
#         raise forms.ValidationError(_(u'Topic message cannot contain the following: %s'%invalid_chars))
#     return topic_message