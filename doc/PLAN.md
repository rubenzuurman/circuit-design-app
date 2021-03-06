# Plan
### Introduction
This document outlines what I want the project to be and how I'm going to accomplish that. <br />

### Project outline
#### Setup
The application can be used to develop logical circuits, a circuit can be exported to a png. It will be some form of block programming; blocks have zero or more inputs and zero or more outputs. The types of blocks in the simulation will be:<br />

- [ ] Logic gate: Has one or more inputs and one output, executes elementary logic.
- [ ] Module: Has zero or more inputs and zero or more outputs, executes logic defined by a script.
- [ ] Subsystem: Has zero or more inputs and zero or more outputs, can contain logic gates, modules and other subsystems, which are internally connected to the inputs and outputs of the subsystem. <br />
- [ ] Switch: Has zero inputs and one output, can be switched on or off by clicking it with the mouse.
- [ ] Lamp: Has one input and one output, provides visual feedback on whether a signal is on or off.

All of these objects will have the same superclass called SimObject. Every SimObject has its own unique identifier. Every SimObject also has a list of tuples containing the output port numbers and the identifiers of the objects to which the inputs of the SimObject are connected, such a tuple is of the form (*object_identifier*, *output_port_number*). It will also have a list containing the boolean values of those outputs. Every SimObject also has a list of booleans representing the state of the outputs, these will be fetched by other SimObjects when needed. The Simulation class will hold a pool of pointers to all of the objects in the simulation, the Subsystem class will have its own internal pool. <br />

#### Running the simulation
When the simulation is run it starts by finding SimObjects which have no outputs connected, this will be Lamps in most cases. For every one of these SimObjects (call it s1) the Simulation will make sure that:<br />

- The SimObject connected to every input (call it s2) is evaluated this iteration.
- The corresponding output of the now evaluated SimObject s2 is copied to the corresponding input of the SimObject s1.

This will start recursive calculation of all necessary SimObjects, leaving isolated blocks out of the calculation which improves performance.

---

# Class setup
## SimObject
### Fields
- *int* identifier
- *bool* evaluated
- *list[tuple]* input_locations
- *list[bool]* input_values
- *list[bool]* output_values
### Functions
- Getters and setters, excluding setter for the identifier.
- *void* set_input_location(_input_port_number, _location): sets the entry of the input locations list with id _input_port_number to _location.
- *void* set_input_value(_input_port_number, _value): sets the entry of the input values list with id _input_port_number to _value.
- *void* add_input(_new_input_port_number): adds extra input to block at the specified place, using the specified port number, pushing ports after the new port down by one.
- *void* add_output(_new_output_port_number): adds extra output to block at the specified place, using the specified port number, pushing ports after the new port down by one.
- *void* connect_input(_input_port_number, _source_id, _source_port_number): connects a specific input to an output port of another block.
- *int* get_num_inputs(): returns the total number of inputs.
- *int* get_num_outputs(): returns the total number of outputs.
- *void* execute_logic(_time): uses the list of input values to determine its output values. This function must be overridden by subclasses.
## Other classes
- Other classes inherit fields and functions from the SimObject class. They call the superconstructor with the number of inputs and outputs required and override the execute_logic() function.
## Simulation
### Fields
- *list[SimObject]* objects
- *float* simulation_time
- *float* simulation_timestep
### Functions
- Getters and setters, excluding setter for the objects list.
- *bool* add_object(_object): adds an object to the simulation, returns true is the action was successful, else returns false.
- *bool* remove_object(_object_id): removes an object from the simulation, returns true is the action was successful, else returns false.
- *void* step(_time): evaluate all objects which no outputs connected.
- *void* step_object(_object, _time): evaluate _object recursively, called from step().