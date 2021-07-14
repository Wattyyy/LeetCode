import os

problems = os.listdir('submissions')
extensions = set()
for name in problems:
    if name == '.DS_Store':
        continue
    path = os.path.join('submissions', name, 'Accepted')
    dirs = os.listdir(path)
    for dir_name in dirs:
        if dir_name == '.DS_Store':
            continue
        for f in os.listdir(path + '/' + dir_name):
            ext = f.split('.')[-1]
            extensions.add(ext)

print(extensions)
        
