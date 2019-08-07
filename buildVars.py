# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon_name" : "dropbox",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : "Dropbox",
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon_description" : _("""Announces Dropbox status or open the Dropbox systray menu.
Shortcut: NVDA+Shift+D"""),
	# version
	"addon_version" : "4.4-dev",
	# Author(s)
	"addon_author" : "Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors",
	# URL for the add-on documentation support
	"addon_url" : "http://addons.nvda-project.org/",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion" : "2019.1",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.3",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "appModules", "*.py"),
    os.path.join("addon", "globalPlugins", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
