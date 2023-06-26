import yaml
from ics import Calendar, Event
import time
import os

# with open('calendar.yaml', 'r', encoding='utf-8') as f:
#     calendar = yaml.safe_load(f)

calendar = None
for dirpath, dirnames, filenames in os.walk('all_info'):
    for file in os.listdir(dirpath):
        if file.endswith('.yaml'):
            with open(os.path.join(dirpath, file), 'r', encoding='utf-8') as f:
                if calendar is None:
                    calendar = yaml.safe_load(f)
                else:
                    calendar['events'].extend(yaml.safe_load(f)['events'])


c = Calendar()
events = calendar['events']
for event in events:
    e = Event()
    e.name = event['school']
    e.begin = event['begin']
    e.end = event['end']
    e.description = event['description'] + '  ' + event['url']
    c.events.add(e)


def delete_files_with_extension(extension):
    current_folder = os.getcwd()  # 获取当前文件夹路径
    for file_name in os.listdir(current_folder):
        if file_name.endswith(extension):
            file_path = os.path.join(current_folder, file_name)
            os.remove(file_path)
            # print(f"Deleted file: {file_path}")


extension = ".ics"
delete_files_with_extension(extension)

# avoid cache
timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename = 'calendar' + timestamp + '.ics'
with open(filename, 'w', encoding='utf-8') as f:
    f.writelines(c.serialize())



usr = 'asimple1'
repo = 'BAOYAN-Calendar'
branch = 'main'
ics_name = filename
# ics_name = 'calendar20230610165344.ics'
url = f"https://open-web-calendar.hosted.quelltext.eu/calendar.html?url=https%3A%2F%2Fraw.githubusercontent.com%2F{usr}%2F{repo}%2F{branch}%2F{ics_name}"

last_update = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 8 * 60 * 60))

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f"""# 上次更新时间：{last_update}\n[![🕊下次一定](img.png "这是一只鸽子")]({url})
    \n# 狠狠点击👆
    \n # 免责声明：本仓库非盈利，对具体内容不承担各项责任
    \n # pr:
    \n 1. fork本仓库
    \n 2. clone到本地,在`all_info`文件夹下创建学校文件夹,并在其中创建学院yaml文件,格式如下:
    \n ```yaml\nevents:\n  - year: "2023"\n    school: "鼠鼠大学"\n    begin: "2023-01-01"\n    end: "2023-01-02"\n    description: "鼠鼠学院"\n    url: "https://www.shushu.edu.cn/"\n```\n
    \n 3. push更新自己的fork,并提交pr
    \n 4. 等待合并
    \n 5. 等待auto update完成后点击鸽鸽
    \n **最后,事关前途,若存在信息错误请及时核实并提issue或pr**
    
    """)


print('done')






