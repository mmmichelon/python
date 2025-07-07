from distutils.dir_util import copy_tree 
import timing 

fromDirectory = "folder 1" 
toDirectory = "folder 2" 

copy_tree(fromDirectory, toDirectory)
