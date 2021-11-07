my_list_str = ['123', '456', '789', '101112', '1314115']
print('-------------------------')
print('my_list_str type: ', type(my_list_str))
new_line_list_str = ', '.join(my_list_str)
print('new line str list: ', new_line_list_str)
print('new line str list type: ', type(new_line_list_str))
my_list_str2 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr']
new_line_list_str += ', '.join(my_list_str2)
print('my_list_str after joining with my_list_str2: ', new_line_list_str)
print('my_list_str type after joining with my_list_str2: ', type(new_line_list_str))

new_dict = {'k1': 100, 'k2': 200, 'k3': 300, 'k4': 400, 'k5': 500}
new_item_testing_list = []
new_testing_list = []
new_testing_dict = {"abc": {"unfulfilled_objectives": ["VIEW_BOOKING_V2", "VIEW_BOOKING", "AGENT_CONNECT_REQUEST", "NEW_BOOKING", "SPEAK_TO_AGENT", "RETRIEVE_BOOKING"], "handled_by_agent": "False", "conversation_itineraries": ["Not Available"]},
                    "def": {"unfulfilled_objectives": ["VIEW_BOOKING_V2", "VIEW_BOOKING", "AGENT_CONNECT_REQUEST", "NEW_BOOKING", "SPEAK_TO_AGENT", "RETRIEVE_BOOKING"], "handled_by_agent": "False", "conversation_itineraries": ["Not Available"]}}
for item in new_dict:
    new_item_testing_list.append(item)
    # print(f'first value in dict: {item}')
    # new_value = ', '.join(item)
    # new_split = ', '.split()
    # print(f'new_value: {new_value}')
    # print(f'new_split: {new_split}')

print('list: ', new_item_testing_list)
print('type of list: ', type(new_item_testing_list))
new_value = ', '.join(new_item_testing_list)
print('new_value: ', new_value)
print('type of new_value: ', type(new_value))


for item in new_testing_dict:
    new_testing_list.append(item)
new_testing_value = ', '.join(new_testing_list)

print('TEST1: ', new_testing_value)
print('TEST: ', new_testing_value.split(':')[0])

test_empty_list = ["Not Available"]
test_not_available = ', '.join(test_empty_list)
print('TEST::: ', test_not_available)

print('-------------------------')