# Plan
### Introduction
This document outlines what I want the project to be and how I'm going to accomplish that. <br />

### Project outline
#### Setup
The application can be used to develop logical circuits, a circuit can be exported to a png. It will be some form of block programming; blocks have zero or more inputs and zero or more outputs. The types of blocks in the simulation will be:<br />

- [ ] Logic gate: Has one or more inputs and one output, executes elementary logic.
- [ ] Module: Has zero or more inputs and zero or more outputs, executes logic defined by a script.
- [ ] Subsystem: Has zero or more inputs and zero or more outputs, can contain logic gates, modules and other subsystems, which are internally connected to the inputs and outputs of the subsystem. <br />
- [ ] Switch: Has zero inputs and one output, can be switched on of off by clicking it with the mouse.
- [ ] Lamp: Has one input and one output, provides visual feedback on whether a signal is on or off.

All of these objects will have the same superclass called SimObject. Every SimObject has its own unique identifier. Every SimObject also has a list of tuples containing the output port numbers and the identifiers the inputs of the SimObject are connected to, such a tuple is of the form (*object_identifier*, *output_port_number*). It will also have a list containing the boolean values of those outputs. Every SimObject also has a list of booleans representing the state of the outputs, these will be fetched by other SimObjects when needed. The Simulation class will hold a pool of pointers to all of the objects in the simulation, the Subsystem class will have its own internal pool. <br />

#### Running the simulation
When the simulation is run it starts by finding SimObjects which has no outputs connected, this will be Lamps in most cases. For these SimObjects the Simulation will make sure the input blocks are run and their inputs will be fetched, which means SimObjects connected to the inputs of these modules will be run if they haven't done so this iteration. This will start recursive calculation of all necessary SimObjects.

---

# Class setup
## SimObject
### Fields
- *int* identifier
- *bool* evaluated
- *list[tuple]* input_pointers
- *list[bool]* input_values
- *list[bool]* output_values
### Functions
- Getters and setters, excluding setter for identifier.
- *void* add_input(): adds extra input to block.
- *void* add_output(): adds extra output to block.
- *int* get_num_inputs(): returns the total number of inputs.
- *int* get_num_outputs(): returns the total number of outputs.
- *void* execute_logic(): uses the set input_values to determine its output_values. This function must be overridden by subclasses.
## Other classes
- Other classes inherit fields and functions from the SimObject class. They call the superconstructor with the number of inputs and outputs required and override the execute_logic() function.