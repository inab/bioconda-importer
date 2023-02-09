import unittest
from glob import glob
from main import get_tool_names, get_type

import json


class TestRecipesRetrieval(unittest.TestCase):

    def test_get_recipes(self):
        """
        Test if the recipes are retrieved from the bioconda repo
        """
        recipes_path = './bioconda-recipes/recipes'
        subdirectories = glob("%s/*/"%(recipes_path))
        tool_names_subs_raw = get_tool_names(subdirectories)
        self.assertTrue(len(tool_names_subs_raw) > 0)


class TestGetType(unittest.TestCase):

    def test_run_host_(self):
        """
        test if a meta.yaml with only host and run listing 
        python/r-base/perl return 'lib'
        """
        with open('./test/data/recipe_only_run_host.json', 'r') as datafile:
            data = json.load(datafile)
        
        types = []
        for package in data:
            types.append(get_type(package))

        self.assertEqual(types, [set(['lib'])])
    
    def test_perl_cmd(self):
        with open('./test/data/recipe_perl_commandline.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(get_type(package))

        self.assertEqual(types, [set(['cmd'])])

    def test_compiled(self):
        with open('./test/data/recipe_compiled.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(get_type(package))

        self.assertEqual(types, [set(['cmd'])])

    def test_lib_imports(self):
        with open('./test/data/recipe_imports.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(get_type(package))

        self.assertEqual(types, [set(['lib'])])

    def test_comd_and_lib_command_and_imports(self):
        with open('./test/data/recipe_command_imports.json', 'r') as datafile:
            data = json.load(datafile)

        types = []
        for package in data:
            types.append(get_type(package))

        self.assertEqual(types, [set(['lib','cmd'])])
        
        
        
        
if __name__ == '__main__':
    unittest.main()