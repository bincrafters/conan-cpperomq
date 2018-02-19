#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, tools
import os


class CpperoMQConan(ConanFile):
    name = "cpperomq"
    version = "0.0.5"
    url = "https://github.com/bincrafters/conan-cpperomq"
    description = "Keep it short"
    license = "MIT"
    exports = ["LICENSE.md"]

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def requirements(self):
        self.requires.add('zmq/[>=4.2.2]@bincrafters/stable')

    def source(self):
        source_url = "https://github.com/jship/cpperomq"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="*.hpp", dst='include', src=include_folder, keep_path=True)
        self.copy(pattern="LICENSE", dst="license", src=self.source_subfolder)

    def package_info(self):
        self.info.header_only()
