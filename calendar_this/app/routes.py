from flask import Blueprint, render_template, request, redirect, url_for
import os
import sqlite3
from datetime import datetime
from .forms import AppointmentForm

bp = Blueprint("main", __name__, url_prefix='/')

DB_FILE = os.environ.get("DB_FILE")

@bp.route("/", methods=['GET', 'POST'])
def main():

    form = AppointmentForm()

    if form.validate_on_submit():
        params = {
            'name': form.name.data,
            'start_datetime': datetime.combine(form.start_date.data, form.start_time.data).strftime('%Y-%m-%d %H:%M:%S'),
            'end_datetime': datetime.combine(form.end_date.data, form.end_time.data).strftime('%Y-%m-%d %H:%M:%S'),
            'description': form.description.data,
            'private': form.private.data
        }

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
            VALUES (:name, :start_datetime, :end_datetime, :description, :private)
        """, params)

        conn.commit()
        conn.close()

        return redirect(url_for('main.main'))

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, start_datetime, end_datetime FROM appointments ORDER BY start_datetime;")
    fetched_rows = cursor.fetchall()
    conn.close()

    rows = []
    for row in fetched_rows:
        id, name, start, end = row
        start_datetime_obj = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        end_datetime_obj = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        rows.append((id, name, start_datetime_obj, end_datetime_obj))

    return render_template("main.html", rows=rows, form=form)
