# importing pandas as pd
import pandas as pd

# CODE 1

# import the StrinIO function
# from io module
from io import StringIO

# wrap the string data in StringIO function
StringData = StringIO("""Date;Event;Cost
	10/2/2011;Music;10000
	11/2/2011;Poetry;12000
	12/2/2011;Theatre;5000
	13/2/2011;Comedy;8000
	""")

# let's read the data using the Pandas
# read_csv() function
df = pd.read_csv(StringData, sep =";")

# Print the dataframe
print(df)
# ----------------------------------------------------------

# CODE 2

# importing pandas as pd
import pandas as pd

# This is our string data
StringData ="""Date;Event;Cost
	10/2/2011;Music;10000
	11/2/2011;Poetry;12000
	12/2/2011;Theatre;5000
	13/2/2011;Comedy;8000
	"""

# Read data
df = pd.read_clipboard(sep = ';')

# Print the DataFrame
print(df)
