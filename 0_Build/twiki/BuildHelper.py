from BasePaths import BasePaths as parent
from Build import Build


class BuildHelper(parent):

    def __init__(self, file, isBuildIncluded):
        super().__init__(file)

        buildPrefix = 'Build.'

        self.build = Build(self.sourceDir, self.destDir, self.version, self.scriptName, self.scriptDescriptor1, self.scriptDescriptor2, isBuildIncluded, buildPrefix)


    def run(self):
        error = self.build.run()
        return error
