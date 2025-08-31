import win32com.client

def list_processes():
    try:
        wmi = win32com.client.GetObject('winmgmts:')
        processes = wmi.ExecQuery("select * from Win32_Process")
        for process in processes:
            print(f'进程ID: {process.Properties_('ProcessID').Value},进程名: {process.Properties_('name').Value}.')
    except Exception as e:
        print(f'错误: {str(e)}')
    
if __name__ == "__main__":
    print("进程列表:")
    list_processes()
