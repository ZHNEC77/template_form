from fastapi import FastAPI, Request, HTTPException
from tinydb import TinyDB, Query
from .validators import get_field_type

app = FastAPI()
db = TinyDB('app/db.json')


@app.post("/get_form")
async def get_form(request: Request):
    try:
        form_data = await request.form()
        form_fields = {key: get_field_type(value)
                       for key, value in form_data.items()}

        templates = db.all()
        for template in templates:
            template_fields = {key: value for key,
                               value in template.items() if key != 'name'}
            if all(field in form_fields and form_fields[field] == template_fields[field] for field in template_fields):
                return template['name']

        return form_fields
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Пример шаблонов форм для инициализации базы данных
db.insert({
    "name": "Order Form",
    "order_date": "date",
    "customer_email": "email",
    "customer_phone": "phone"
})

db.insert({
    "name": "Contact Form",
    "contact_name": "text",
    "contact_email": "email"
})
