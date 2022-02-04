# Alekya Billakanti
import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 14 ) : 
     world_rank,institution,country,national_rank,quality_of_education,alumni_employment,quality_of_faculty,publications,influence,citations,broad_impact,patents,score,year = datalist

    # print intermediate key-value pairs to standard output
  print(country,"\t",1)
















