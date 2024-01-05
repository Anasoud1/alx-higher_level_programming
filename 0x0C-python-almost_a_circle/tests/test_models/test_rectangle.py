#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
import io
import sys

class TestRectangle_instantiation(unittest.TestCase):
	'''class TestRectangle instantiation'''
	def test_no_arg(self):
		'''test with no arg'''
		with self.assertRaises(TypeError):
			Rectangle()

	def test_one_arg(self):
		'''test one arg'''
		with self.assertRaises(TypeError):
			Rectangle(1)

	def test_two_arg(self):
		'''test 2 argument'''
		r1 = Rectangle(10, 2)
		r2 = Rectangle(2, 10)
		self.assertEqual(r1.id, r2.id - 1)

	def test_three_args(self):
		r1 = Rectangle(2, 2, 4)
		r2 = Rectangle(4, 4, 2)
		self.assertEqual(r1.id, r2.id - 1)

	def test_four_args(self):
		r1 = Rectangle(1, 2, 3, 4)
		r2 = Rectangle(4, 3, 2, 1)
		self.assertEqual(r1.id, r2.id - 1)

	def test_five_args(self):
		self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

	def test_more_than_five_arg(self):
		with self.assertRaises(TypeError):
			Rectangle(10, 2, 0, 0, 7, 2)

	def test_width_private(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(5, 5, 0, 0, 1).__width)

	def test_height_private(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(5, 5, 0, 0, 1).__height)

	def test_x_private(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(5, 5, 0, 0, 1).__x)

	def test_y_private(self):
		with self.assertRaises(AttributeError):
			print(Rectangle(5, 5, 0, 0, 1).__y) 

	def test_width_getter(self):
		r = Rectangle(5, 2, 3, 4, 1)
		self.assertEqual(5, r.width)

	def test_setter_width(self):
		r1 = Rectangle(1, 2, 3, 4)
		r1.width = 11
		self.assertEqual(r1.width, 11)

	def test_height_getter(self):
		r = Rectangle(5, 7, 7, 5, 1)
		self.assertEqual(7, r.height)

	def test_height_setter(self):
		r = Rectangle(5, 7, 7, 5, 1)
		r.height = 10
		self.assertEqual(10, r.height)

	def test_x_getter(self):
		r = Rectangle(5, 7, 7, 5, 1)
		self.assertEqual(7, r.x)

	def test_x_setter(self):
		r = Rectangle(5, 7, 7, 5, 1)
		r.x = 10
		self.assertEqual(10, r.x)

	def test_y_getter(self):
		r = Rectangle(5, 7, 7, 5, 1)
		self.assertEqual(5, r.y)

	def test_y_setter(self):
		r = Rectangle(5, 7, 7, 5, 1)
		r.y = 10
		self.assertEqual(10, r.y)

	def test_first_arg_string(self):
		with self.assertRaises(TypeError):
			Rectangle("string", 2, 0, 0, 7)

	def test_second_arg_string(self):
		with self.assertRaises(TypeError):
			Rectangle(10, "string", 0, 0, 7)

	def test_third_arg_string(self):
		with self.assertRaises(TypeError):
			Rectangle(10, 1, "0", 0, 7)

	def test_forth_arg_string(self):
		with self.assertRaises(TypeError):
			Rectangle(10, 1, 0, "0", 7)

	def test_first_arg_negative(self):
		with self.assertRaises(ValueError):
			Rectangle(-10, 1)

	def test_second_arg_negative(self):
		with self.assertRaises(ValueError):
			Rectangle(10, -1)

	def test_first_arg_equal_to_zero(self):
		with self.assertRaises(ValueError):
			Rectangle(0, 1)

	def test_second_arg_equal_to_zero(self):
		with self.assertRaises(ValueError):
			Rectangle(1, 0)

	def test_third_arg_negative(self):
		with self.assertRaises(ValueError):
			Rectangle(1, 1, -2)

	def test_forth_arg_negative(self):
		with self.assertRaises(ValueError):
			Rectangle(1, 1, 1, -2)

class TestRectangle_function(unittest.TestCase):
	'''TestRectangle_function class'''
	@staticmethod
	def capture_stdout(rect, method):
		"""Captures and returns text printed to stdout.

		Args:
			rect (Rectangle): The Rectangle to print to stdout.
			method (str): The method to run on rect.
		Returns:
			The text printed to stdout by calling method on sq.
		"""
		capture = io.StringIO()
		sys.stdout = capture
		if method == "print":
			print(rect)
		else:
			rect.display()
		sys.stdout = sys.__stdout__
		return capture

	def test_area(self):
		r = Rectangle(2, 3)
		self.assertEqual(r.area(), 6)

	def test_str_(self):
		r = Rectangle(4, 6, 2, 1, 12)
		self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

	def test_dispaly_no_xy(self):
		r = Rectangle(3, 2)
		capture = TestRectangle_function.capture_stdout(r, "display")
		self.assertEqual(capture.getvalue(), "###\n###\n")

	def test_dispaly_no_y(self):
		r = Rectangle(3, 2, 1)
		capture = TestRectangle_function.capture_stdout(r, "display")
		self.assertEqual(capture.getvalue(), " ###\n ###\n")

	def test_dispaly_with_xy(self):
		r = Rectangle(3, 2, 1, 1)
		capture = TestRectangle_function.capture_stdout(r, "display")
		self.assertEqual(capture.getvalue(), "\n ###\n ###\n")
