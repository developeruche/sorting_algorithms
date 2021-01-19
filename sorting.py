""" This sorting algorithm works with in built Python sorting method """
def sort_with_time(e):
    return e['time']
    
list_test = [
    {
        "time": 5,
        "text": 'testing time five'
    },
        {
        "time": 10,
        "text": 'testing time ten'
    },
        {
        "time": 1,
        "text": 'testing time one'
    },
        {
        "time": 3,
        "text": 'testing time three'
    },
        {
        "time": 45,
        "text": 'testing time forty-five'
    },
]

# Sorting the list_test with the time 


list_test.sort(key=sort_with_time)

print(list_test)