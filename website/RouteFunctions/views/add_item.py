
import os
from uuid import uuid4
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from ... import db, base_dir

from website.models import Item
img_formats = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
valid_category = ['tech', 'garden', 'books', 'sports']


@login_required
def add_item():
    if request.method == "POST":
        category = request.form.get('category')
        name = request.form.get('name')
        description = request.form.get("description")
        price = request.form.get('price')
        image = request.files['image']

        if validate_data(category, name, description, price, image):
            print('yes')
            img_ext = image.filename.split(".")
            fileName = str(uuid4()) + "." + img_ext[-1]
            image.save(os.path.join(base_dir, f"static/Pictures/{fileName}"))

            item = Item(user_id=current_user.id, category=category,
                        image=fileName, name=name, description=description, price=price)
            db.session.add(item)
            return redirect(url_for("views.home"))
    return render_template('Views/add_item.html', user=current_user)


def validate_data(cat, name, desc, prc, img):
    valid = True

    if cat not in valid_category:
        flash('Please Select Valid Category', category='error')
        valid = False
    if len(name) > 60 or len(name) < 5:
        flash('Item Name Must Be Between 5 And 60 Characters', category='error')
        valid = False
    if len(desc) > 500 or len(desc) < 10:
        flash('Item Description Must Be Between 10 And 500 Characters',
              category='error')
        valid = False
    try:
        if int(prc) < 0:
            flash('Item Price Must Be Positive Number', category='error')
            valid = False
    except ValueError:
        flash('Item Price Must Be Positive Number', category='error')
        valid = False
    if not img or not img.filename.lower().endswith(img_formats):
        flash("Upload Correct Image File Type", category='error')
        valid = False
    return valid
