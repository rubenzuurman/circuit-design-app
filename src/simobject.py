class SimObject:
	"""
	Parent class of all objects in the simulation.
	"""

	# Holds the identifier of the SimObject that will be created next.
	NEXT_ID = 0

	def __init__(self, _num_inputs, _num_outputs):
		"""
		Initializes object id, inputs and outputs.
		"""
		# Check parameter types.
		err_msg_num_inputs = "SimObject.__init__(): Parameter " \
			"_num_inputs be a nonnegative integer."
		err_msg_num_outputs = "SimObject.__init__(): Parameter " \
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
		"""Returns this SimObject's identifier."""
		return self.id_

	def get_evaluated(self):
		"""Returns this SimObject's evaluated boolean."""
		return self.evaluated

	def get_input_locations(self):
		"""Returns this SimObject's input locations."""
		return self.input_locations

	def get_input_values(self):
		"""Returns this SimObject's input values."""
		return self.input_values

	def get_output_values(self):
		"""Returns this SimObject's output values."""
		return self.output_values

	def get_num_inputs(self):
		"""Returns the number of inputs."""
		return len(self.get_input_values())

	def get_num_outputs(self):
		"""Returns the number of outputs."""
		return len(self.get_output_values())

	# Setters
	def set_evaluated(self, _evaluated):
		"""Sets evaluated boolean."""
		# Check parameter type.
		err_msg_eval = "SimObject.set_evaluated(): Parameter _evaluated " \
			"must be a boolean."
		assert isinstance(_evaluated, bool), err_msg_eval

		# Set evaluated boolean.
		self.evaluated = _evaluated

	def set_input_locations(self, _input_locations):
		"""Sets input locations list. It's generally better to set these one 
		by one using the method set_input_location()."""
		# Check parameter type.
		err_msg_inp_locs = "SimObject.set_input_locations(): Parameter " \
			"_input_locations must be a list of tuples containing " \
			"integers."
		assert isinstance(_input_locations, list), err_msg_inp_locs
		for entry in _input_locations:
			assert isinstance(entry, tuple), err_msg_inp_locs
			for entry2 in entry:
				assert isinstance(entry2, int), err_msg_inp_locs

		# Set input locations list.
		self.input_locations = _input_locations

	def set_input_location(self, _input_port_number, _location):
		"""Sets the entry of the input locations list with id 
		_input_port_number to _location."""
		# Check parameter types.
		err_msg_inp_port_num = "SimObject.set_input_location(): Parameter " \
			"_input_port_number must be a nonnegative integer."
		err_msg_inp_port_num_invalid = "SimObject.set_input_location(): " \
			"Parameter _input_port_number must be a valid input port."
		err_msg_loc = "SimObject.set_input_location(): Parameter " \
			"_location must be a tuple of integers."
		assert isinstance(_input_port_number, int), err_msg_inp_port_num
		assert _input_port_number < self.get_num_inputs(), \
			err_msg_inp_port_num_invalid
		assert isinstance(_location, tuple), err_msg_loc
		for entry in _location:
			assert isinstance(entry, int), err_msg_loc

		# Set input location.
		self.input_locations[_input_port_number] = _location

	def set_input_values(self, _input_values):
		"""Sets input values list. Useful when testing a custom module for 
		example."""
		# Check parameter type.
		err_msg_inp_vals = "SimObject.set_input_values(): Parameter " \
			"_input_values must be a list of booleans."
		assert isinstance(_input_values, list), err_msg_inp_vals
		for entry in _input_values:
			assert isinstance(entry, bool), err_msg_inp_vals

		# Set input values list.
		self.input_values = _input_values

	def set_input_value(self, _input_port_number, _value):
		"""Sets the entry of the input values list with id 
		_input_port_number to _value."""
		# Check parameter types.
		err_msg_inp_port_num = "SimObject.set_input_value(): Parameter " \
			"_input_port_number must be a nonnegative integer."
		err_msg_inp_port_num_invalid = "SimObject.set_input_value(): " \
			"Parameter _input_port_number must be a valid input port."
		err_msg_val = "SimObject.set_input_value(): Parameter _value " \
			"must be a boolean."
		assert isinstance(_input_port_number, int), err_msg_inp_port_num
		assert _input_port_number < self.get_num_inputs(), \
			err_msg_inp_port_num_invalid
		assert isinstance(_value, bool), err_msg_val

		# Set input value.
		self.input_values[_input_port_number] = _value

	def set_output_values(self, _output_values):
		"""Sets output values list."""
		# Check parameter type.
		err_msg_out_vals = "SimObject.set_output_values(): Parameter " \
			"_output_values must be a list of booleans."
		assert isinstance(_output_values, list), err_msg_out_vals
		for entry in _output_values:
			assert isinstance(entry, bool), err_msg_out_vals

		# Set output values list.
		self.output_values = _output_values

	# Other functions
	def add_input(self, _new_input_port_number):
		"""Adds an extra input to the block at the specified place, using the 
		specified port number, pushing ports after the new port down by 
		one."""
		# Check parameter type.
		err_msg_port_num = "SimObject.add_input(): Parameter " \
			"_new_input_port_number must be a nonnegative integer."
		assert isinstance(_new_input_port_number, int), err_msg_port_num
		assert _new_input_port_number >= 0, err_msg_port_num

		# Split input locations and input values lists at the specified
		# index.
		loc_list_left = self.get_input_locations()[:_new_input_port_number]
		loc_list_right = self.get_input_locations()[_new_input_port_number:]

		val_list_left = self.get_input_values()[:_new_input_port_number]
		val_list_right = self.get_input_values()[_new_input_port_number:]

		# Join split lists using (-1, -1) and False respectively.
		new_loc_list = loc_list_left + [(-1, -1)] + loc_list_right
		new_val_list = val_list_left + [False] + val_list_right

		# Set input locations list and input values list equal to new lists.
		self.set_input_locations(new_loc_list)
		self.set_input_values(new_val_list)

	def add_output(self, _new_output_port_number):
		"""Adds an extra output to the block at the specified place, using the 
		specified port number, pushing ports after the new port down by 
		one."""
		# Check parameter type.
		err_msg_port_num = "SimObject.add_output(): Parameter " \
			"_new_output_port_number must be a nonnegative integer."
		assert isinstance(_new_output_port_number, int), err_msg_port_num
		assert _new_output_port_number >= 0, err_msg_port_num

		# Split output values list at the specified index.
		val_list_left = self.get_output_values()[:_new_output_port_number]
		val_list_right = self.get_output_values()[_new_output_port_number:]

		# Join split list using False.
		new_val_list = val_list_left + [False] + val_list_right

		# Set output values list equal to new list.
		self.set_output_values(new_val_list)

	def connect_input(self, _input_port_number, _source_id, _source_port_number):
		"""Creates a connection between the specified output port of the 
		SimObject with identifier `_source_id` and the specified input port
		of this SimObject. If either of the ports or a SimObject with the 
		specified identifier do not exist the connection will either not be 
		created or not executed."""
		# Check parameter types.
		err_msg_inp_port_num = "SimObject.connect_input(): Parameter " \
			"_input_port_number must be a nonnegative integer " \
			"representing an input port of this object."
		err_msg_src_id = "SimObject.connect_input(): Parameter " \
			"_source_id must be a nonnegative integer."
		err_msg_src_port_num = "SimObject.connect_input(): Parameter " \
			"_source_port_number must be a nonnegative integer."
		assert isinstance(_input_port_number, int), err_msg_inp_port_num
		assert isinstance(_source_id, int), err_msg_src_id
		assert isinstance(_source_port_number, int), err_msg_src_port_num
		assert _input_port_number >= 0 \
			and _input_port_number < self.get_num_inputs(), \
			err_msg_inp_port_num
		assert _source_id >= 0, err_msg_src_id
		assert _source_port_number >= 0, err_msg_src_port_num

		# Set input location.
		self.set_input_location(_input_port_number, \
			(_source_id, _source_port_number))

		# Reset input value.
		self.set_input_value(_input_port_number, False)

	def execute_logic(self, _time):
		pass