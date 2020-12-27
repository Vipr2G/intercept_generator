# intercept_generator
Generates intercepts with parameters randomized around user provided seed values
This was written using python 3.73 and has also run in 3.8.X

There are 3 files associated with the intercept_generator:
  intercept_generator.py
  parameter_generator.py 
  intercept.json
  
intercept.json is edited by the user to configure the intercept_generator's run. 
Variables to pay attention to are in EMITTER.GENERAL if the intercept.json file
and include:
  ELNOT
  number_of_intercepts
  output_file_name
  domain
  
  
Variables in the EMITTER.PARAMETERS section allow the user to configure the parametric
values of the intercepts to be created. This is where the user will assign desired
seed values to be randomized for the intecepts actual parameters. For example, under PRI
the user sets:
  number_of_pris: (Not really used and should be cleaned up)
  modulation_type: (Currently set to STAGGER, and I do NO checking to see if the modType makes sense)
  distribution: (Currently set to normal) controls the type of randomize algorithm (Normal, Gaus...)
  tolerance: A bad variable name as I intened it to be "slop" around the given seed value, but in fact
    it changes depending on the distribution chosen. Example, if distrobution=NORMAL then tolerance is really
    "Sigma" where 2 would be 2 standard deviations. 
  data: The actuall values to be used to seed the random number generator for the intercepts. In the example 
  we will build 100 emitters, ALL with the same elnot, all having 10 pris randomly generated about 
  400.0, 450.0, 500.0 etc.
  
  
To execute the program, cd into the directory contaiing the 3 files and type:
python intercept_generator

The output will be a json file named in the intercept.json file. 
Note that you will need to remove the last coma in the json file to have it properly formatted.

Note that I've commented out the last 3 lines. Put them back in to see a depiction of the randomizer at work
in a histogram.

  
