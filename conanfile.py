from conans import ConanFile, tools
import os


class CpperoMQConan(ConanFile):
    name = "cpperomq"
    version = "0.0.5"
    url = "https://github.com/bincrafters/conan-cpperomq"
    description = "Keep it short"
    license = "MIT"
    exports = ["LICENSE.md"]

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def requirements(self):
        self.requires.add('zeromq/4.3.2')

    def source(self):
        source_url = "https://github.com/jship/cpperomq"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "CpperoMQ-" + self.version

        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="*.hpp", dst='include', src=include_folder, keep_path=True)
        self.copy(pattern="LICENSE", dst="license", src=self._source_subfolder)

    def package_info(self):
        self.info.header_only()
