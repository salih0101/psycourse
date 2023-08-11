from aiogram.dispatcher.filters.state import State, StatesGroup


class UserRegistration(StatesGroup):
    getting_name_state = State()
    getting_phone_number = State()
    getting_location = State()
    getting_gender = State()

class Category(StatesGroup):
    get_category = State()
    get_subcategory = State()


class Settings(StatesGroup):
    set_setting = State()
    set_name_setting = State()
    set_number_setting = State()
    set_name = State()
    set_number = State()

class Uz_Settings(StatesGroup):
    uz_set_setting = State()
    uz_set_name_setting = State()
    uz_set_number_setting = State()
    uz_set_name = State()
    uz_set_number = State()

class Menu(StatesGroup):
    main_menu_state = State()


class Subscription(StatesGroup):
    check_subscription = State()


class Channel_sub_check(StatesGroup):
    check_sub_channel = State()

