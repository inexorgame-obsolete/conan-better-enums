from conans import ConanFile, tools
import os


class BetterenumsConan(ConanFile):
	name = "better-enums"
	version = "0.11.1"
	license = "BSD 2-clause"
	url = "https://github.com/aantron/better-enums"
	# No settings/options are necessary, this is header only

	def source(self):
		self.run("git clone https://github.com/aantron/better-enums.git")
		self.run("cd better-enums && git checkout tags/0.11.1")

	def package(self):
		self.copy("*.h", "include")
