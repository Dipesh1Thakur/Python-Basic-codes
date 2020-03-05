# searching data
students_info={'steven':9888,'Harry':9876545,'Abdul':78987}
print(students_info)
students_info['Harry']
# students_info['Hari']
search_key='Harry' #input  ("Enter the number of students :")
if search_key in students_info:
    print(search_key,students_info[search_key])
else:
    print(search_key, "not found")
    print(len(students_info))

# deleting
if search_key in students_info:
    del students_info[search_key]
print(students_info)
print(students_info)
        # print(len(students_info))