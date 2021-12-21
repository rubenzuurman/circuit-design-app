class SimObject:
	"""
	Parent class of all objects in the simulation.
	"""

	# Holds the identifier of the SimObject that will be created next.
	NEXT_ID = 0

	def __init__(self, _num_inputs, _num_outputs):
		"""
		Initializes necessary fields.
		"""
		# Check parameter types.
		err_msg_num_inputs = "SimObject.__init__(): Paremeter _num_inputs " \
			"be a nonnegative integer."
		err_msg_num_outputs = "SimObject.__init__(): Paremeter " \
			"_num_outputs be a nonnegative integer."
		assert isinstance(_num_inputs, int), err_msg_num_inputs
		assert isinstance(_num_outputs, int), err_msg_num_outputs
		assert _num_inputs >= 0, err_msg_num_inputs
		assert _num_outputs >= 0, err_msg_num_outputs

		# Init object identifier.
		self.id_ = SimObject.NEXT_ID
		SimObject.NEXT_ID += 1

		# Init evaluated bool.
		self.evaluated = False

		# Init inputs and outputs.
		self.input_locations = [(-1, -1)] * _num_inputs
		self.input_values = [False] * _num_inputs

		self.output_values = [False] * _num_outputs

	# Getters
	def get_id(self):
		return self.id_

	def get_evaluated(self):
		return self.evaluated

	def get_input_locations(self):
		return self.input_locations

	def get_input_values(self):
		return self.input_values

	def get_output_values(self):
		return self.output_values

	# Setters.
	def set_evaluated(self, _evaluated):
		# Check parameter type.
		err_msg_eval = "SimObject.set_evaluated(): Parameter _evaluated " \
			"must be a boolean."
		assert isinstance(evaluated, bool), err_msg_eval

		self.evaluated = _evaluated

	def set_input_locations(self, _input_locations):
		# Check parameter type.
		err_msg_inp_locs = "SimObject.set_evaluated(): Parameter " \
			"_input_locations must be a list of tuples containing " \
			"positive integers."
		assert isinstance(_input_locations, list), err_msg_inp_locs
		for entry in _input_locations:
			assert isinstance(entry, tuple), err_msg_inp_locs
			for entry2 in entry:
				assert isinstance(entry2, int), err_msg_inp_locs
				assert entry2 >= 0, err_msg_inp_locs

		self.input_locations = _input_locations

	def set_input_values(self, _input_values):
		# Check parameter type.
		err_msg_inp_vals = "SimObject.set_evaluated(): Parameter " \
			"_input_values must be a list of booleans."
		assert isinstance(_input_values, list), err_msg_inp_vals
		for entry in _input_values:
			assert isinstance(entry, bool), err_msg_inp_vals

		self.input_values = _input_values

	def set_output_values(self, _output_values):
		# Check parameter type.
		err_msg_out_vals = "SimObject.set_evaluated(): Parameter " \
			"_output_values must be a list of booleans."
		assert isinstance(_output_values, list), err_msg_out_vals
		for entry in _input_values:
			assert isinstance(entry, bool), err_msg_out_vals

		self.output_values = _output_values