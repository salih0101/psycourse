from aiogram import Dispatcher, executor, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from states import UserRegistration, Category, Settings, Menu, Subscription, Channel_sub_check
#from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
import buttons as btns
import database
import states
import time
import os
import logging
import inline_buttons as course
import strings_uz.uz_inline_buttons as uzcourse
import strings_uz.uz_buttons as uzbtns
from strings_uz import uz_inline_buttons
from strings_uz import uz_buttons
from strings_uz.uz_list_course import *