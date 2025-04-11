from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для хранения данных пользователей
users_data = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Добавляем данные в список
        users_data.append({
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        })

        # Перенаправляем на ту же страницу (чтобы избежать повторной отправки формы при обновлении)
        return redirect(url_for('index'))

    # Отображаем шаблон с текущими данными
    return render_template('index.html', users=users_data)


if __name__ == '__main__':
    app.run(debug=True)