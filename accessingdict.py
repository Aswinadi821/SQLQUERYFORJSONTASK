import json
with open('Input_2.json') as json_content:
    read_content = json.load(json_content)
val2= input()
val3=input()
def getvaluebycomponent(read_content,val2,val3):
    for key,value in read_content.items():
           if type(value) is dict:
              getvaluebycomponent(value,val2,val3)

           elif type(value) is type(list()) and type(value[0]) is dict:
                if (value[0][val2]) == val3:
                      print(value[0])

                elif (value[1][val2]) == val3:
                     print(value[1])
def getsqlfunc(jsonvalue):
    sql="""SELECT * FROM stats
           JOIN diagnosis
           ON stats.component = diagnosis.component
           WHERE component = stats
           CREATE TABLE unioncomponents
              SELECT * FROM TABLE stats
              UNION
             SELECT * FROM TABLE diagnosis;"""
    return sql

jsonvalue=getvaluebycomponent(read_content,val2,val3)
print(getsqlfunc(jsonvalue))

