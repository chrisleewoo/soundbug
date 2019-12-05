# soundbug
The audible debugger

Transforms a python function or entire program into a midi file. Code changed to music!
This can be useful for debugging or understanding data flow, but it still could be imporved upon.

Thanks to VishnuBob for the wonderful python midi library
https://github.com/vishnubob/python-midi

Use command.x to automatically redirect inputs from Trace.py > Dis.py > MidiGen.py

See the .DAT files for reading the outputs of trace and dis functions

6	28-E1	Break 	*bassish
	
2	67-G4	ROT	

3	31-G1	LOAD (Pushes)	
9	31-G1	Make (Pushes)
 
1	43-G2	POP

5	45-A2	Get 	

8	52-E3	Delete	

11	60-C4	ALU

7	64-E4	Continue 			

10	76-E5	Import 		

4	84-C6	STORE	

SLICE is commented out since it seems to dominate. 
The SLICE command in CPython seems to be used to divide up or add to the top of the stack (TOS).
