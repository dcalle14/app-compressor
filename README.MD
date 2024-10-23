Project developed by Mario Fernando Andrade Rojas e Isabella Ceballos Bedoya

# Text compressor and decompressor.

Data compression is the reduction of the volume of data that can be processed to represent a certain information using a smaller amount of space. In this project, the use of RLE compression or Run-length encoding is a very simple form of data compression in which data sequences with the same consecutive value are stored as a single value plus its count.

## How do we make it work?

- Prerequisites: 
	1. Have the latest available versions of Python and pip installed.

	2. You have 2 options, it is recommended to use the virtual environment.
		1. You will need to create a virtual environment using virtualenv, run the following commands 1 by 1:
			- src\console\rle_compression_console.py 

			- After creating the virtual environment and activating it you should see something similar to this:
				- (my_project) text-compressor-main1 

			- Install the necessary libraries to run the project:
				- psycopg2 <pre>pip install psycopg2</pre>
				
		2.Perform all of the following procedure without creating the virtual environment:

			- Instalar la libreria psycopg2-binary

				- To install it through pip, run the following command in your preferred terminal:
				<pre>pip install psycopg2-binary</pre>

				- For more information consult the original documentation: https://www.psycopg.org/docs/
	
	3. Have a database in Neon Tech

		- To create it you must go to the official Neon Tech website: https://neon.tech.

			1. You must log in to their website, or register if you do not have an account created.

			2. You create a new project.
			
			3. You go to the section that says "Dashboard".
			
			4. In the Database section, select the database where you want to save the database and its information.

			5. Click where it says "ConnectionString", a menu will be displayed.
			
			6. Select the one that says "Parameters only".
			
		- What to do with the information?

			1. Once the page shows you the database parameters, go to the "src" folder.

			2. There you must enter the "controller" folder.
			
			3. In the controller folder, enter the "secret_config_example" file.
			
			4. Finally you must follow the steps indicated in the 'secret_config_example.py' file to continue
			with the database connection process.
```
text-compressor-main1/
├── .vscode
│   └── settings.json
├── sql
│     ├── crear-tablas.sql
│
├── src
│   ├── console
│   │    └── rle_compression_console.py
│   │    
│   ├── controller
│   |   └──controlador_tabla.py
│   |            
│   ├── functionalities
│   |   ├── _init_.py
│   |   └── rle_compression.py          
│   │    
│   └── gui 
│   │   ├── _init_.py
│   │   └── rle_compression_gui.py      
│   │
│   ├──model
│   └── palabra_comprimida.py    
│   │  
│   ├──view_console 
│   └── crear-tabla.py     
│ 
├──test 
│   ├── database_test.py
│   └── rle_compression.py 
│
├── .gitignore    # Paths excluded from version control
├── LICENSE       
└── README.md     
```

## ¿Cómo usar el programa?

- Before running any command, you need to make a copy of the 'secret_config_example.py' file and rename it as follows:
'secret_config.py', inside this file that you copied is where you will insert your NeonTech credentials to be able to use the database. If this step is not done the program will not work.


- To run the encryption program from the console interface, you must enter the following command:
	- <pre>python app.py</pre>

## How to run the tests?

To execute the test cases you must write the following commands in the python terminal:
- This will run the test cases for the encryption engine:
<pre>python tests/database_test</pre>

- This will execute the test cases for the database:
<pre>python tests/rle_compression_tests.py</pre>

