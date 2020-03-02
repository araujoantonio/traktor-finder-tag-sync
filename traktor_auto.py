import os
# import sys

def readTags(file_path):
    command = ('tag -lN "' + file_path + '"')
    print(command)
    stream = os.popen(command)
    output = stream.read()
    return output

folder = input('Which folder you whish to scan, Mr. Antonio?\n')
stream = os.popen('ls -d /Users/antonioaraujo/Music/' + folder + '/*')
# stream = os.popen('ls -d /Users/antonioaraujo/Music/deep/*')
output = stream.readlines()

for file_path in output:
    file_path = file_path.replace('\n', '')
    # print(file_path)
    readTags(file_path)
    

def writeComments(tags):
    pass    
    



# musics = ['teste1', 'teste2']

# musics = shell_output.strip()

# for file in musics:
#     print("music " + musics.index(file))
    # read tag
    # append tag to comment

