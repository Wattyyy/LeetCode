import os
import shutil
import glob

# problems = os.listdir('submissions')
# notuse = ['Output Limit Exceeded', 'Compile Error', 'Memory Limit Exceeded']
# for name in problems:
#     if name == '.DS_Store':
#         continue
#     for rm_dir in notuse:
#         if os.path.exists( os.path.join('submissions', name, rm_dir) ):
#             shutil.rmtree( os.path.join('submissions', name, rm_dir) )

st = set()
problems = os.listdir('submissions')
for name in problems:
    if name == '.DS_Store':
        continue
    for fname in os.listdir('submissions/' + name):
        st.add(fname)
print(st)
    



# problems = os.listdir('submissions')
# for name in problems:
#     if name == '.DS_Store':
#         continue
#     path = os.path.join('submissions', name, 'Accepted')
#     dirs = os.listdir(path)
#     for dir_name in dirs:
#         if dir_name == '.DS_Store':
#             continue
#         if ',' not in dir_name:
#             continue
#         mdy, other = dir_name.split(',')
#         m, d, y = mdy.split('-')
#         new_name = y + m.zfill(2) + d.zfill(2) + other
#         os.rename(os.path.join(path, dir_name), os.path.join(path, new_name))



# 'javascript', 'txt', 'rust', 'python', 'c', 'mysql', 'python3'
# conversion = {
#     'python3': 'py', 
#     'python': 'py', 
#     'c': 'c',
#     'rust': 'rs',
#     'javascript': 'js',
#     'mysql': 'sql'
# }

# problems = os.listdir('submissions')
# for name in problems:
#     if name == '.DS_Store':
#         continue
#     path = os.path.join('submissions', name, 'Accepted')
#     dirs = sorted(os.listdir(path), reverse=True)
#     for dir_name in dirs:
#         if dir_name == '.DS_Store':
#             continue
#         for file in glob.glob( os.path.join(path, dir_name)+'/Solution*' ):
#             try:
#                 shutil.move(file, path)
#             except:
#                 continue
        

# problems = os.listdir('submissions')
# for name in problems:
#     if name == '.DS_Store':
#         continue
#     path = os.path.join('submissions', name, 'Accepted')
#     for file in glob.glob( path + '/Solution*' ):
#         shutil.move(file, os.path.join('submissions', name))
        




