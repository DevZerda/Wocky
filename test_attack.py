import os, sys, time

from assets.api_attack_system.main import *

print(APICrud.GetAPIWithMethod(sys.argv[1]))