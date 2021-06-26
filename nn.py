import os, sys, time

from assets.api_attack_system.main import *

# print(APICrud.listAPIs())

# print(APICrud.GetAPI("SST"))

print(APICrud.GetAPIWithMethod(sys.argv[1]))