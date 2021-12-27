from simobject import SimObject

class Simulation:
	"""
	Class holding the entire simulation, at the highest level responsible 
	for running the logic.
	"""

	def __init__(self, _simulation_starttime, _simulation_timestep, \
		_simulation_endtime):
		"""Initializes objects list and time management variables."""
		# Set objects list.
		self.objects = []

		# Set time management variables.
		self.simulation_starttime = _simulation_starttime
		self.simulation_endtime = _simulation_endtime

		self.simulation_time = _simulation_starttime
		self.simulation_timestep = _simulation_timestep
		self.simulation_maxtime = _simulation_endtime

	# Getters
	def get_objects(self):
		"""Returns the list of objects."""
		return self.objects

	def get_simulation_time(self):
		"""Returns the current simulation time."""
		return self.simulation_time

	def get_simulation_timestep(self):
		"""Returns the simulation timestep."""
		return self.simulation_timestep

	# Setters
	def set_simulation_time(self, _simulation_time):
		"""Sets the simulation time."""
		# Check parameter type.
		err_msg_simtime = "Simulation.set_simulation_time(): Parameter " \
			"_simulation_time must be a nonnegative float."
		assert isinstance(_simulation_time, float) \
			or isinstance(_simulation_time, int), err_msg_simtime
		assert _simulation_time >= 0, err_msg_simtime

		# Set simulation time.
		self.simulation_time = _simulation_time

	def set_simulation_timestep(self, _simulation_timestep):
		"""Sets the simulation timestep."""
		# Check parameter type.
		err_msg_simtimestep = "Simulation.set_simulation_timestep(): " \
			"Parameter _simulation_timestep must be a nonnegative float."
		assert isinstance(_simulation_timestep, float) \
			or isinstance(_simulation_timestep, int), err_msg_simtimestep
		assert _simulation_timestep >= 0, err_msg_simtimestep

		# Set simulation timestep.
		self.simulation_timestep = _simulation_timestep

	# Other functions
	def add_object(self, _object):
		"""Add object to the simulation. Fails if an object with the same 
		identifier already exist or if _object is not a SimObject."""
		# Check parameter type.
		err_msg_obj = "Simulation.add_object(): Parameter _object must be " \
			"SimObject or a subclass thereof."
		assert isinstance(_object, SimObject), err_msg_obj

		# Check object id against existing objects.
		for obj in self.get_objects():
			if obj.get_id() == _object.get_id():
				print("Simulation.add_object(): SimObject with identifier " \
					f"{obj.get_id()} already exists!")
				return False

		# Add object to objects list.
		self.objects.append(_object)
		print("")
		return True

	def remove_object(self, _object_id):
		"""Remove object with identifier _object_id from the simulation. 
		Fails if an object with the identifier _object_id is not present in 
		the simulation."""
		# Check parameter type.
		err_msg_obj_id = "Simulation.remove_object(): Parameter " \
			"_object_id must be a nonnegative integer."
		assert isinstance(_object_id, int), err_msg_obj_id
		assert _object_id >= 0, err_msg_obj_id

		# Check object id against existing objects.
		for obj in self.get_objects():
			if obj.get_id() == _object.get_id():
				print(f"Object with identifier {_object.get_id()} removed " \
					"from simulation.")
				return True

		print("Simulation.remove_object(): SimObject with identifier " \
			f"{obj.get_id()} does not exist!")
		return False

	def step(self, _time):
		""""""
		pass