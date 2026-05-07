import gspread
import os
from dotenv import load_dotenv

load_dotenv()

class GoogleSheetsService:
    def __init__(self):
        try:
            import os
            creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json")
            self.gc = gspread.service_account(filename=creds_path)
            self.sheet = self.gc.open(os.getenv("SHEET_NAME")).sheet1
        except Exception as e:
            print(f"Ошибка подключения к Google Таблицам: {e}")
            self.sheet = None

    async def add_booking(self, data: dict):
        if not self.sheet:
            return False
            
        # Проверка на дубликаты
        records = self.sheet.get_all_records()
        for row in records:
            if str(row.get('Телефон')) == str(data['phone']) and str(row.get('Дата')) == str(data['date']):
                return False # Уже записан
        
        self.sheet.append_row([
            data.get('name'), data.get('phone'), 
            data.get('service'), data.get('date'), data.get('time')
        ])
        return True

gs_service = GoogleSheetsService()