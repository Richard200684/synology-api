from synology_api import downloadstation


# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will login automatically

# fl = filestation.FileStation('192.168.1.16', '5000', 'Angela', '@ng3l@_99_vdk')
# fl.get_info()
def my_script_function():
    dwn = downloadstation.DownloadStation('', '5000', '', 'LulDeBeh@nger#84', debug=False)
    # dwn.get_info()
    tasks = dwn.tasks_list()

    # Remove the trailing comma and space
    result = '\n'.join(data['title'] + ' - ' + data['status'] for data in tasks['data']['tasks'])
    print(result)
    # return result


my_script_function()
