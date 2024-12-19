##create classes 
#class to read and assess values for a pdf document
#subclass to separate between controls, cases, solvents, etc

# ask user whether it's a quant or screen
# ask user to set batch number
# ask user to set directory where pdfs are located


# compile list of pdfs to be used from directory

#BatchClass
# bind sequence to back of batch pack
# bind curve to front of batch pack

#Doc Class
# pass doc into reader inside try block
#     assign values based on py reading the doc
    
# self.case number #must be present
# self.extract #base or acid, can be None
# self.pages
# print all assignments
# print exceptions

# find case number, sample type, batch number
# assess if qc or unknown + reinject

# class(QC)
#     bind docs as batch number - date
#     list controls
#     list cals
#     append to list and then export to excel sheet

# class(unknown)
#     bind docs - label with case number and batch number
#     if base and acid, bind base then acid
#     find