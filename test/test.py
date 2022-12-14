import unittest

import bioconda_imp
import bioconda_imp.importer_recipes as bioc
import json


class TestGetType(unittest.TestCase):

    def test_run_host_(self):
        """
        test if a meta.yaml with only host and run listing 
        python/r-base/perl return 'lib'
        """
        with open('data/recipe_only_run_host.json', 'r') as datafile:
            data = json.load(datafile)
        
        types = []
        for package in data:
            types.append(bioc.get_type(package))

        self.assertEqual(types, [set(['lib'])])
    
    def test_perl_cmd(self):
        with open('data/recipe_perl_commandline.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(bioc.get_type(package))

        self.assertEqual(types, [set(['cmd'])])

    def test_compiled(self):
        with open('data/recipe_compiled.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(bioc.get_type(package))

        self.assertEqual(types, [set(['cmd'])])

    def test_lib_imports(self):
        with open('data/recipe_imports.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(bioc.get_type(package))

        self.assertEqual(types, [set(['lib'])])

    def test_comd_and_lib_command_and_imports(self):
        with open('data/recipe_command_imports.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(bioc.get_type(package))

        self.assertEqual(types, [set(['lib','cmd'])])
        
        
        
        
if __name__ == '__main__':
    unittest.main()