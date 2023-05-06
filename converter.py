import pandas as pb

df = pb.read_csv('c:\WaFuelPUP.csv')

df.to_html('c:\WaFuelULP.html')
