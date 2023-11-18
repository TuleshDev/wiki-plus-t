import os.path

from BaseTools import BaseTools


class BasePaths:

    def __init__(self, file):
        self.rootDir = os.path.dirname(file)

        sourceFragment = ''
        path = os.path.join(self.rootDir, 'source.txt')
        if os.path.exists(path):
            with open(path, 'r') as read_file:
                sourceFragment = read_file.readline().replace('\n', '')

        if sourceFragment == '':
            self.sourceDir = os.path.join(self.rootDir, 'sourceDir')
        else:
            self.sourceDir = BaseTools.buildPath(self.rootDir, sourceFragment)

        destFragment = ''
        path = os.path.join(self.rootDir, 'destination.txt')
        if os.path.exists(path):
            with open(path, 'r') as read_file:
                destFragment = read_file.readline().replace('\n', '')

        if destFragment == '':
            self.destDir = os.path.join(self.rootDir, 'destDir')
        else:
            destFragment = BaseTools.buildPath(self.rootDir, destFragment)
            self.destDir = destFragment

        #path = os.path.join(self.rootDir, 'version.txt')
        #if os.path.exists(path):
        #    with open(path, 'r') as read_file2:
        #        self.version = read_file2.readline().replace('\n', '')
        #else:
        #    self.version = ''
        self.version = ''

        self.scriptName = 'twiki'

        self.scriptDescriptor1 = self.scriptName + '.' + self.scriptName
        self.scriptDescriptor2 = self.scriptDescriptor1
