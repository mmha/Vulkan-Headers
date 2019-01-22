from conans import ConanFile, tools, CMake
import os


class VulkanHeadersConan(ConanFile):
    name = "vulkan-headers"
    version = "1.1.97"
    description = "Vulkan Header files and API registry"
    url = "https://github.com/KhronosGroup/Vulkan-Headers"
    exports_sources= "*", "!.git"
    header_only = True
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
