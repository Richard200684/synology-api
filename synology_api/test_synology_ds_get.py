from synology_api import downloadstation

# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will login automatically

# fl = filestation.FileStation('', '5000', '', '')

# fl.get_info()

dwn = downloadstation.DownloadStation('', '5000', '', '', debug=False)

# dwn.get_info()
# data = dwn.tasks_list()
json_output = dwn.tasks_list()
for data in json_output['data']['tasks']:
    print(data['title'] + ' - ' + data['status'])
    # for task in data['status']:
    #     print(task)
# print(json_output)

# for key in json_output.keys():
#     print(key, json_output[key])
# print_nested_json(json_output)
