from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from complaint_bot.database import save_complaint

router = Router()

class ComplaintForm(StatesGroup):
   name = State()
   contact = State()
   complaint = State()

def skip_keyboard():
   return ReplyKeyboardMarkup(
      keyboard=[[KeyboardButton(text="Пропустить")]],
      resize_keyboard=True
   )

@router.message(Command("complaint"))
async def complaint_start(message: Message, state: FSMContext):
   await state.set_state(ComplaintForm.name)
   await message.answer("Введите ваше имя:", reply_markup=skip_keyboard())

@router.message(ComplaintForm.name, F.text)
async def process_name(message: Message, state: FSMContext):
   if message.text != "Пропустить":
      await state.update_data(name=message.text)
   else:
      await state.update_data(name="Не указано")
   await state.set_state(ComplaintForm.contact)
   await message.answer("Введите ваш контакт (телефон или аккаунт):", reply_markup=skip_keyboard())

@router.message(ComplaintForm.contact, F.text)
async def process_contact(message: Message, state: FSMContext):
   if message.text != "Пропустить":
      await state.update_data(contact=message.text)
   else:
      await state.update_data(contact="Не указано")
   await state.set_state(ComplaintForm.complaint)
   
   await message.answer("Опишите вашу жалобу:", reply_markup=ReplyKeyboardRemove())

@router.message(ComplaintForm.complaint, F.text)
async def process_complaint(message: Message, state: FSMContext):
   await state.update_data(complaint=message.text)
   data = await state.get_data()
   save_complaint(data)
   await state.clear()
   await message.answer("Ваша жалоба успешно сохранена. Спасибо!")
