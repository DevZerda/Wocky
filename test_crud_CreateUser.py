import os, sys, time

from assets.auth.crud import *

print(CRUD.CreateUser("newUser", "newPassword", 1, 600, 0))